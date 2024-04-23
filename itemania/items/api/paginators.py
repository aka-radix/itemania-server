from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 8

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "page": self.page.number,
                "results": data,
            },
        )
