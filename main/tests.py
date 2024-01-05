from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import CovidCase


class CovidCaseViewSetTests(APITestCase):

    def setUp(self):
        self.covid_case1 = CovidCase.objects.create(
            case_id='Case 1',
            age=66,
            gender='M',
            nationality='Chinese',
            imported_local='Imported',
            place='Wuhan',
            public_healthcare_institution='Singapore General Hospital',
            status='Hospitalised',
            date_of_confirmation='2020-01-23',
            date_of_discharge=None,
            places_visited='Shangri-La Rasa Sentosa Resort & Spa',
            residing_location='N/A',
            residing_postal_code='98970',
            reference_url='https://www.moh.gov.sg/news-highlights/details/confirmed-imported-case-of-novel-coronavirus-infection-in-singapore-multi-ministry-taskforce-ramps-up-precautionary-measures'
        )

        self.covid_case2 = CovidCase.objects.create(
            case_id='Case 2',
            age=53,
            gender='F',
            nationality='Chinese',
            imported_local='Imported',
            place='Wuhan',
            public_healthcare_institution='National Centre for Infectious Disease',
            status='Discharged',
            date_of_confirmation='2020-01-24',
            date_of_discharge='2020-02-07',
            places_visited='Raffles Hospital, Tan Tock Seng Emergency Department, Orchard Road, Marina Bay Sands, Gardens by the Bay',
            residing_location='J8 hotel, 8 Townshend Road',
            residing_postal_code='207606',
            reference_url='https://www.moh.gov.sg/news-highlights/details/two-more-cases-of-confirmed-imported-case-of-novel-coronavirus-infection-in-singapore'
        )

        self.covid_case3 = CovidCase.objects.create(
            case_id='Case 3', age=37, gender='M', nationality='Chinese',
            imported_local='Imported', place='Wuhan', public_healthcare_institution='Singapore General Hospital',
            status='Hospitalised', date_of_confirmation='2020-01-24', date_of_discharge=None,
            places_visited='N/A', residing_location='N/A', residing_postal_code='0',
            reference_url='https://www.moh.gov.sg/news-highlights/details/two-more-cases-of-confirmed-imported-case-of-novel-coronavirus-infection-in-singapore'
        )

    def test_list_covid_cases(self):
        url = reverse('main:covidcase-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_covid_case(self):
        url = reverse('main:covidcase-detail', args=[self.covid_case1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['case_id'], 'Case 1')
        self.assertEqual(response.data['age'], 66)

    def test_create_covid_case(self):
        url = reverse('main:covidcase-list')
        data = {
            'case_id': 'Case 4',
            'age': 42,
            'gender': 'F',
            'nationality': 'Indian',
            'imported_local': 'Imported',
            'place': 'Delhi',
            'public_healthcare_institution': 'AIIMS',
            'status': 'Hospitalised',
            'date_of_confirmation': '2022-01-05',
            'date_of_discharge': None,
            'places_visited': 'N/A',
            'residing_location': 'New Delhi',
            'residing_postal_code': '110001',
            'reference_url': 'https://example.com'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CovidCase.objects.count(), 4)

    def test_update_covid_case(self):
        url = reverse('main:covidcase-detail', args=[self.covid_case1.id])
        data = {'age': 67, 'status': 'Discharged'}

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.covid_case1.refresh_from_db()
        self.assertEqual(self.covid_case1.age, 67)
        self.assertEqual(self.covid_case1.status, 'Discharged')

    def test_delete_covid_case(self):
        url = reverse('main:covidcase-detail', args=[self.covid_case2.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CovidCase.objects.count(), 2)
