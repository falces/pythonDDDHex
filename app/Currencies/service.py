from app import app, signals
import uuid
from .entities import Currency

def importCurrenciesService(repository) -> list:
    providerCurrencies = repository.getCurrencies()
    currencies = []
    for providerCurrency in providerCurrencies:
        currency = Currency(
            id = providerCurrency['id'],
            isoCode = providerCurrency['iso4217_currency_code'],
            description = providerCurrency['description'],
            active = providerCurrency['active'],
        ).toDict()

        signals['new_currency_received'].send(
            sender=uuid.uuid4().hex,
            message=currency,
        )

        currencies.append(currency)
    app.logger.info("Total currencies imported: %s", len(currencies))
    return currencies

def saveCurrency(
    repository,
    currencyDTO: list,
):
    currency = Currency(
        id = currencyDTO['id'],
        isoCode = currencyDTO['isoCode'],
        description = currencyDTO['description'],
        active = currencyDTO['active'],
    )

    repository.save(currency)
