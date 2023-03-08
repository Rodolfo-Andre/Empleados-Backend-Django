from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
  def get_paginated_response(self, data):
        return Response({
            'pagination': {
              'current_page': self.page.number,
              'page_size': self.page_size,
              'count_per_page': self.page.__len__(),
              'num_pages': self.page.paginator.num_pages,
              'next': self.get_next_link(),
              'previous': self.get_previous_link(),
              'count': self.page.paginator.count
            },
            'results': data
        })