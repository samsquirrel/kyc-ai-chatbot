def verify_document(text):

    if "ID" in text or "Passport" in text:
        return "Document appears to be a valid identity document."

    return "Unable to verify document."