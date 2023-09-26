#!/usr/bin/env sh
set -e

function run() {
    spider=$1
    echo "\n ℹ️  Run spider: $spider\n"
    hatch run crawl:run ${spider} \
      && printf "\n\
        🌟 spider $spider executed successfully!\n"\
      || printf "\n\
        💥 Error when running spider $spider 💥\n"

}

function runall() {
    spiders=`scrapy list`
    for spider in ${spiders[@]}; do
        run spider
    done

}

if [ $# -eq 0 ]; then
    set -- runall
else
    set -- run "$1"
fi
