-- 1. Assicurati che l'estensione pgvector sia abilitata
-- Puoi farlo dalla UI di Supabase in Database > Extensions

-- 2. Crea la tabella per memorizzare gli embeddings degli schemi
CREATE TABLE schema_embeddings (
  id BIGSERIAL PRIMARY KEY,
  schema_name TEXT NOT NULL,
  content TEXT NOT NULL,
  embedding VECTOR(768) -- I modelli di embedding di Gemini usano 768 dimensioni
);

-- 3. Crea una funzione per la ricerca di similarità (RPC)
-- Questo rende le query dal client Python molto più pulite
CREATE OR REPLACE FUNCTION match_schemas (
  query_embedding VECTOR(768),
  match_threshold FLOAT,
  match_count INT
)
RETURNS TABLE (
  id BIGINT,
  schema_name TEXT,
  content TEXT,
  similarity FLOAT
)
LANGUAGE sql STABLE
AS $$
  SELECT
    se.id,
    se.schema_name,
    se.content,
    1 - (se.embedding <=> query_embedding) AS similarity
  FROM schema_embeddings se
  WHERE 1 - (se.embedding <=> query_embedding) > match_threshold
  ORDER BY similarity DESC
  LIMIT match_count;
$$;
