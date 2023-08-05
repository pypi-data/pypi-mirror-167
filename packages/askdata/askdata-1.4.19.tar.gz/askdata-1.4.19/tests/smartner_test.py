from askdata.human2query import smartner, smartner_automated_analysis
import time

if __name__ == "__main__":

    # Prod
    # token = ""
    # datasets = ["619247D0-CD55-40AA-9B76-09A3BA1AC6DB-MYSQL-024cbe97-00a0-46b0-8252-333351238d9a", "619247D0-CD55-40AA-9B76-09A3BA1AC6DB-MYSQL-d8288331-1ae7-45f7-b129-e726c0634b94"]
    # language = "en"
    # env = "prod"

    # Dev
    token = ""
    datasets = ["f2c705dd-f63f-475b-95a9-c1ad20f33716-CSV-0bc30f26-9feb-4da4-a7e1-500f58871909", "f2c705dd-f63f-475b-95a9-c1ad20f33716-CSV-f5bf15de-ae34-423b-8406-816c379c1bc8", "f2c705dd-f63f-475b-95a9-c1ad20f33716-CSV-b95abad6-46a2-4202-a003-d33a9bf2ba9d", "f2c705dd-f63f-475b-95a9-c1ad20f33716-CSV-550bc190-967c-4b39-9c3c-265c9069c1db", "f2c705dd-f63f-475b-95a9-c1ad20f33716-DATA_TABLE-2c2921d2-eb54-4c1e-94ff-d2886515bbee", "f2c705dd-f63f-475b-95a9-c1ad20f33716-DATA_TABLE-e32fcefd-329a-47d8-a7af-b587c016cc65", "f2c705dd-f63f-475b-95a9-c1ad20f33716-DATAFRAME-956cc090-3992-4745-b677-c5efcccee445", "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-835ec991-69cc-4636-a899-4d0d518ebb56", "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-34b83631-1108-41c3-870f-cee0636c58c7", "f2c705dd-f63f-475b-95a9-c1ad20f33716-EXCEL-a47a3e04-13d3-4d3a-bac2-299dbd946e26", "f2c705dd-f63f-475b-95a9-c1ad20f33716-EXCEL-c2785009-8a48-4377-9bf8-216d1f1be3fd", "f2c705dd-f63f-475b-95a9-c1ad20f33716-DATA_TABLE-c116fcb8-770d-4a3b-8769-2c6a0817da36", "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-7bc8aa74-134a-4e93-b5db-8ea42e309496", "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-70c82ef8-2cb2-40dd-a92f-b49a80d0a305", "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-2338a078-0949-4662-a4a6-7f0e2685154b", "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-5a758aa2-14ef-4aa5-adbc-a6b38e7f1638", "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-2492f8d5-b569-4ae9-9728-ccfd43b27e95"]
    language = "en"
    env = "dev"

    # Usage
    nl = "download"

    start = time.time()
    smartquery_list = smartner(nl=nl, token=token, datasets=datasets, language=language, env=env, use_cache=False,
                               response_type="anonymize")
    end = time.time()
    for sq in smartquery_list:
        print(sq)
        print()

    print("Time: ", end-start, "s")
    print()

    suggestions = [["{{dimension.A}} and {{measure.A}}", {"{{measure.A}}": {"code": "DOWNLOAD", "value": "Download", "dataset": "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-70c82ef8-2cb2-40dd-a92f-b49a80d0a305"}, "{{dimension.A}}": {"code": "WEB SITE", "value": "Web site", "dataset": "f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-70c82ef8-2cb2-40dd-a92f-b49a80d0a305"}}, ["f2c705dd-f63f-475b-95a9-c1ad20f33716-MYSQL-70c82ef8-2cb2-40dd-a92f-b49a80d0a305"]]]

    start = time.time()
    smartquery_list = smartner_automated_analysis(suggestions, token, env="dev", response_type="deanonymize")
    end = time.time()

    print("Automated analysis")
    for sq in smartquery_list:
        print(sq)
        print()

    print("Time: ", end - start, "s")

