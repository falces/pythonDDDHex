from Infrastructure.Controller.CountryController import CountryController

class App:
    def __init__(self, countryController: CountryController):
        self.countryController = countryController

    def run(self):
        countries = self.countryController.getCountries()
        for country in countries:
            print(country)
            
if __name__ == "__main__":
    from Infrastructure.Repository.CountryRepository import CountryRepository
    from Application.CountryService import CountryService

    # Initialize the repository and service
    country_repository = CountryRepository()
    country_service = CountryService(country_repository)

    # Initialize the controller with the service
    country_controller = CountryController(country_service)

    # Create the app instance and run it
    app = App(country_controller)
    app.run()