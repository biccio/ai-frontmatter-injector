import os

import ai_core
import file_handler


def process_folder(root_path, llm_config, schema_collection, product_info, force=False, dry_run=False):
    """
    Logica principale per elaborare i file in una cartella locale.
    Questa funzione è riutilizzabile sia per lo script locale che per quello di GitHub.
    """
    prompt_template, kb_content = ai_core.load_prompt_and_knowledge_base()
    markdown_files = file_handler.scan_markdown_files(root_path)
    total_files = len(markdown_files)
    print(f"[+] Trovati {total_files} file Markdown da elaborare in '{root_path}'.")

    summary = {
        "processed": 0,
        "updated": 0,
        "skipped": 0,
        "failed": 0
    }

    for i, file_path in enumerate(markdown_files):
        relative_path = os.path.relpath(file_path, root_path)
        print(f"\n--- Elaborazione di: {relative_path} ({i+1}/{total_files}) ---")
        summary["processed"] += 1
        
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if not content.strip():
                print("  -> File vuoto. Saltato.")
                summary["skipped"] += 1
                continue

            print("  -> Ricerca schemi pertinenti su ChromaDB...")
            schema_context = ai_core.retrieve_relevant_schemas(schema_collection, content)
            print("  -> Contesto recuperato. Generazione frontmatter in corso...")

            generated_yaml_str = ai_core.generate_frontmatter(
                llm_config, prompt_template, schema_context, kb_content, content, product_info
            )

            if not generated_yaml_str:
                print("  -> Errore: L'AI non ha restituito un output.")
                summary["failed"] += 1
                continue
            
            validated_frontmatter = ai_core.validate_and_parse_yaml(generated_yaml_str)

            if validated_frontmatter:
                if not dry_run:
                    was_updated = file_handler.update_file_with_frontmatter(
                        file_path, validated_frontmatter, force
                    )
                    if was_updated:
                        print("  -> File aggiornato con successo.")
                        summary["updated"] += 1
                    else:
                        summary["skipped"] += 1
                else:
                    print("  -> DRY-RUN: Frontmatter generato e valido.")
            else:
                print("  -> Errore: L'output dell'AI non è un YAML valido.")
                summary["failed"] += 1
        
        except Exception as e:
            print(f"  -> Errore imprevisto durante l'elaborazione del file: {e}")
            summary["failed"] += 1
    
    return summary
