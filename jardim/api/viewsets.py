from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jardim.models import esp8266Test


@api_view(['POST', ])
def test_post(self):
    no_data = 'no_data'
    if self.method == "POST":
        print('received post')
        data = self.data.get('test', no_data)
        print("data", data)
        if data != no_data:
            test = esp8266Test()
            test.info = data
            test.save()
        return Response(data, status=status.HTTP_200_OK)