"""Simple command-line example for Custom Search.
Command-line application that does a search.
"""

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

import pprint

from apiclient.discovery import build


def main(apiKey, q):
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.

  service = build("customsearch", "v1",
            developerKey=apiKey)

  res = service.cse().list(
      q=q,
      cx='015267152292348546700:l1jzt9ewozi',

    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main('AIzaSyAOcDshR94ts5dab94LT3BlrKlE82nYIlI', 'avinash+sivaraman')
