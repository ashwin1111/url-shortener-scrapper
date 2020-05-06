# Website-Details-Scrapping-API
The API created using the flask and beautifulsoup helps to get the description of the website address given.

This API is used to get the details of the URL's given by the user to create their own collection in URL Shortner (https://urlll.xyz). 

This service helps https://urlll.xyz 's API to run a Job every x hours to scrap website titles and description

Payload: https://webpage-details.herokuapp.com/get_page_details?web_address=https://covid19-india-stat.herokuapp.com/
 
Response:
 
{
"data":
      {
        "first_p_tag":["Today"],
        "meta_data":["Dashboard that gives live tracking of COVID-19 India"],
        "title":["COVID-19 India"]
      }
}
