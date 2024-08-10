def individual_serial(template) -> dict:
    return {
        "id": str(template["_id"]),
        "nome": template['nome'],
        "musculo": template["musculo"],
        "info": template["info"],
        "dicas": template["dicas"],
    }

def list_serial(templates) -> list:
    return [individual_serial(template) for template in templates]