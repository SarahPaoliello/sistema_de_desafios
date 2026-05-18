from database.conexao import supabase


def listar_desafios():

    res = (
        supabase.table("desafios")
        .select("*")
        .execute()
    )

    return res.data


def participar_desafio(desafio_id, usuario_id):

    return (
        supabase.table("participantes_desafio")
        .insert({
            "desafio_id": desafio_id,
            "usuario_id": usuario_id
        })
        .execute()
    )
