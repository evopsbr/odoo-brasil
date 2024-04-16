{  # pylint: disable=C8101,C8103
    "name": "Odoo Next - Address Extension",
    "description": "Modifies address forms",
    "version": "17.0.1.0.1",
    "category": "Localization",
    "author": "Trustcode",
    "license": "OEEL-1",
    "contributors": [
        "Luciano Vicentini <lvicentini@evops.com.br>",
        "Walisson Tirtao Sobral <wsobral@evops.com.br>",
        "Paulo Victor Aoki <paoki@evops.com.br>",
    ],
    "depends": [
        "account",
        "l10n_br_base",
        "base_address_extended",
    ],
    "data": [
        "data/configuration.xml",
        "data/res.country.csv",
        "data/res.country.state.csv",
        "views/res_partner.xml",
        "views/res_city.xml",
        "views/res_company.xml",
    ],
    "post_init_hook": "post_init",
}
