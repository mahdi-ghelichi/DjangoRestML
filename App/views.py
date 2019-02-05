import pickle
from rest_framework.response import Response
from rest_framework import views
from App.serializers import RFModelSerializer
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from rest_framework import status


class Train(views.APIView):
    def post(self, request):
        iris = datasets.load_iris()
        X, y = iris.data, iris.target
        name = request.data.pop('name')

        try:
            clf = RandomForestClassifier(**request.data)
            clf.fit(X, y)

        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        serializer = RFModelSerializer(data={'model': pickle.dumps(clf), 'name': name})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


