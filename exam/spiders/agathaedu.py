import re
from typing import Type, Self

from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Response

from exam.items import ExamItem


class AgathaeduSpider(CrawlSpider):
    name = 'agathaedu'
    allowed_domains = ['projetoagathaedu.com.br']
    start_urls = ['https://www.projetoagathaedu.com.br/banco-de-questoes.php']

    rules = (
        Rule(LinkExtractor(restrict_css='div.lista-icones')),
        Rule(LinkExtractor(restrict_css='.opcao'), callback='parse_questions'),
    )

    def parse_questions(self: Self, response: Type[Response]):
        matter = (
            response.css('.topo > a:nth-child(3)::text')
            .get(default='*')
            .strip()
        )
        topic = (
            response.css('.questao-vestibular-titulo::text')
            .get(default='*')
            .strip()
        )

        answers = response.css('#gabarito td::text').re(r'\d{1,2}\.\w')

        for selector in response.css('.questoes-enem-vestibular'):
            item = ExamItem()

            item['matter'] = matter
            item['topic'] = topic
            item['url'] = response.url

            yield from self.parse_question(selector, item, answers)

    def parse_question(
        self: Self,
        selector: Selector,
        item: ExamItem,
        answers: list[str],
    ):
        item['difficulty'] = 'Média'

        item['enunciation'] = ' '.join(
            p.strip()
            for p in selector.css(
                'p:not(.questoes-enem-vestibular-foco)::text'
            ).getall()
        )

        item['alternatives'] = [
            alternative.strip()
            for alternative in selector.css('ol li::text').getall()
        ]  # ajustar para ter as opções ('A': 1, 'B': 12, 'C': 42)
        item['multiple_choice'] = True
        item['enunciation_image'] = selector.css('img::attr(src)').get()
        item['image_answer'] = ''
        item['answer'] = self.get_answer(item['enunciation'], answers)
        item['origin'] = self.get_origin(item['enunciation'])
        item['release_date'] = ''

        yield item

    def get_answer(self, enunciation: str, answers: list[str]) -> None | str:
        result = re.search(r'^\d\.', enunciation)
        if not result:
            return

        number = result.group()
        answer = [
            re.sub(r'\d\.', '', answer)
            for answer in answers
            if answer.startswith(number)
        ]

        if not answer:
            return

        return answer[0]

    def get_origin(self, enunciation: str) -> None | str:
        result = re.search(r'\d\. \((?P<origin>.*)\)', enunciation)
        if not result:
            return
        return result.group('origin')
