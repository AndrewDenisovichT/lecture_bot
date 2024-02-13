from site_API.utils.site_api_handler import SiteApiInterface

headers = {
    "X-RapidAPI-Key": "6e348bb4c6msh11716c4b0d05df2p1d26ecjsn56358afbb9f5",
    "X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

url = "https://" + headers["X-RapidAPI-Host"]

params = {"fragment": "true", "json": "true"}

site_api = SiteApiInterface()

if __name__=='__main__':
    site_api()