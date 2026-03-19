from typing import Any, Generator

import scrapy
from scrapy.http import Response


class CoursesSpider(scrapy.Spider):
    name = "courses"
    allowed_domains = ["mate.academy"]
    start_urls = ["https://mate.academy/"]

    def parse(
            self,
            response: Response,
            **kwargs
    ) -> Generator[dict[str, Any], Any, None]:
        for course in response.css(".ProfessionCard_cardWrapper__BCg0O"):
            name = course.css(".ProfessionCard_title__m7uno span::text").get()
            short_description = course.css(
                ".ProfessionCard_description__K8weo"
                "::text"
            ).get()
            duration = course.css(
                ".ProfessionCard_duration__13PwX::text"
            ).get()

            yield {
                "name": name,
                "short_description": short_description,
                "duration": duration[0],
            }
