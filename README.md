# Website-Details-Scrapping-API
The API created using the flask and beautifulsoup helps to get the description of the website address given.

This API is used to get the details of the URL's given by the user to create their own collection in URL Shortner (https://app.urlll.xyz/short-url). 
 
 For exmaple if we need to get the details of URL- https://covid19-india-stat.herokuapp.com/

 The response will be obtained as follows:
 
 {"data":
      {
        "first_p_tag":["Today"],
        "meta_data":["Dashboard that gives live tracking of COVID-19 India"],
        "title":["COVID-19 India"]
      }
}
