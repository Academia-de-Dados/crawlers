import re
from datetime import UTC, datetime
from string import ascii_uppercase
from typing import Self

from scrapy import Selector
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from exam.items import ExamItem


class AgathaeduSpider(CrawlSpider):
    name = 'agathaedu'
    allowed_domains = ['projetoagathaedu.com.br']
    start_urls = ['https://www.projetoagathaedu.com.br/banco-de-questoes.php']

    rules = (
        Rule(LinkExtractor(restrict_css='div.lista-icones')),
        Rule(LinkExtractor(restrict_css='.opcao'), callback='parse_questions'),
    )

    def parse_questions(self: Self, response: Response):
        matter = re.sub(
            r'>',
            '',
            response.css('.topo > a:nth-child(3)::text').get(default='*'),
        ).strip()
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
                'p:not(.questoes-enem-vestibular-foco)::text',
            ).getall()
        )

        item['alternatives'] = [
            {option: alternative.strip()}
            for option, alternative in zip(
                ascii_uppercase,
                selector.css('ol li::text').getall(),
                strict=False,
            )
        ]
        item['multiple_choice'] = True
        item['enunciation_image'] = selector.css('img::attr(src)').get()
        item['image_answer'] = ''
        item['answer'] = self.get_answer(item['enunciation'], answers)
        item['origin'] = self.get_origin(item['enunciation'])
        item['release_date'] = self.get_release_date(item['origin'])

        yield item

    def get_answer(self, enunciation: str, answers: list[str]) -> None | str:
        result = re.search(r'^\d\.', enunciation)
        if not result:
            return None

        number = result.group()
        answer = [
            re.sub(r'\d\.', '', answer)
            for answer in answers
            if answer.startswith(number)
        ]

        if not answer:
            return None

        return answer[0]

    def get_origin(self, enunciation: str) -> None | str:
        result = re.search(r'\d\. \((?P<origin>.*)\)', enunciation)
        if not result:
            return None
        return result.group('origin')

    def get_release_date(self: Self, origin: None | str) -> None | datetime:
        if (
            not origin
            or not (result := re.search(r'\w (?P<year>\d{,4})', origin))
            or not (year := result.group('year'))
        ):
            return None

        return datetime(int(year), 1, 1, tzinfo=UTC)
