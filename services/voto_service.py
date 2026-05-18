from database.conexao import supabase


def votar(usuario_id, participante_id, voto):

    existe = (
        supabase.table("votos")
        .select("id")
        .eq("usuario_id", usuario_id)
        .eq("participante_id", participante_id)
        .execute()
    )

    if existe.data:
        return "Você já votou"

    supabase.table("votos").insert({
        "usuario_id": usuario_id,
        "participante_id": participante_id,
        "voto": voto
    }).execute()

    return "ok"
