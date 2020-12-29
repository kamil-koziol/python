from typing import Dict, Optional


class MailReciever:
    def __init__(self, address: str, variables: Optional[Dict[str, str]]):
        self.address = address
        self.variables = variables

    def get_prepared_html(self, html: str):
        for variable in self.variables:
            replace_variable = "{{ " + variable + " }}"
            html = html.replace(replace_variable, self.variables.get(variable))

        return html

    def __repr__(self):
        return self.address
