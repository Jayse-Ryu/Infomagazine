from bson import ObjectId
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, renderer_classes
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.utils import json

import v1.permissions as custom_permissions
from v1.landingpage.models import LandingPage
from v1.landingpage.utils import LandingPages


class LandingPageViewSets(viewsets.ViewSet):
    landing_pages_model = LandingPage(choice_db='infomagazine')
    permission_classes = (custom_permissions.IsMarketer,)

    def list(self, request):
        projection = {'_id': 1, 'landing_info.landing.name': 1, 'landing_info.landing.views': 1}
        data = self.landing_pages_model.list(choice_collection='landing_pages', projection=projection)
        result = (
            {
                'state': True,
                'data': json.loads(data),
                'message': 'success'
            },
            {'status': status.HTTP_201_CREATED}
        )

        if not data:
            result = ({}, {'status': status.HTTP_503_SERVICE_UNAVAILABLE})
        return Response(result[0], **result[1])

    def create(self, request):
        body = json.loads(request.body)
        document = {
            "company_id": body['company_id'],
            "landing_info": body['landing_info'],
            "updated_date": body['updated_date']
        }
        data = self.landing_pages_model.create(choice_collection='landing_pages', document=document)

        result = (
            {
                'state': True,
                'data': None,
                'message': 'success'
            },
            {'status': status.HTTP_201_CREATED}
        )

        if not data:
            result = ({}, {'status': status.HTTP_503_SERVICE_UNAVAILABLE})
        return Response(result[0], **result[1])

    def retrieve(self, request, pk):
        data = self.landing_pages_model.retrieve(choice_collection='landing_pages', doc_id=pk)
        result = (
            {
                'state': True,
                'data': json.loads(data),
                'message': 'success'
            },
            {'status': status.HTTP_201_CREATED}
        )

        if not data:
            result = ({}, {'status': status.HTTP_503_SERVICE_UNAVAILABLE})
        return Response(result[0], **result[1])

    def update(self, request, pk):
        data = self.landing_pages_model.update(choice_collection='landing_pages', doc_id=pk,
                                               update={'$set': request.data})
        result = (
            {
                'state': True,
                'data': json.loads(data),
                'message': 'success'
            },
            {'status': status.HTTP_201_CREATED}
        )

        if not data:
            result = ({}, {'status': status.HTTP_503_SERVICE_UNAVAILABLE})
        return Response(result[0], **result[1])

    # TODO AllowAny 지워야 함
    @action(detail=True, methods=['GET'], permission_classes=[permissions.AllowAny])
    def preview(self, request, pk):
        if not pk:
            result = ({
                          'state': False,
                          'data': "",
                          'message': 'not set "pk"'
                      },
                      {'status': status.HTTP_400_BAD_REQUEST})
            return Response(result[0], **result[1])

        try:
            landing_info = json.loads(self.landing_pages_model.retrieve(choice_collection='landing_pages', doc_id=pk))
            if landing_info:
                # # TODO request landing_info로 바꿔야 함
                # with open('test.json') as data_file:
                #     landing_info = json.load(data_file)

                landing_pages = LandingPages(landing_info['landing_info'])
                result = (
                    {
                        'state': True,
                        'data': landing_pages.generate(),
                        'message': 'success'
                    },
                    {'status': status.HTTP_200_OK})
            else:
                result = ({
                              'state': False,
                              'data': "",
                              'message': pk + ' don\'t exist'
                          },
                          {'status': status.HTTP_500_INTERNAL_SERVER_ERROR})
            return Response(result[0], **result[1])
        except Exception as e:
            result = (
                {
                    'state': False,
                    'data': '',
                    'message': str(e)
                },
                {'status': status.HTTP_500_INTERNAL_SERVER_ERROR})
            return Response(result[0], **result[1])
