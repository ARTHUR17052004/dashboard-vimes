def gerar_resumo_por_vime(vime: str, ano: str):

    dados = {
        "2024": {
            "VIME I": gerar_dados_base(10, 2),
            "VIME II": gerar_dados_base(8, 1),
            "VIME III": gerar_dados_base(12, 3),
            "VIME IV": gerar_dados_base(9, 2),
            "VIME V": gerar_dados_base(11, 1),
            "VIME VI": gerar_dados_base(7, 1),
            "VIME VII": gerar_dados_base(13, 4),
        },
        "2025": {
            "VIME I": gerar_dados_base(10, 1),
            "VIME II": gerar_dados_base(8, 2),
            "VIME III": gerar_dados_base(12, 2),
            "VIME IV": gerar_dados_base(9, 1),
            "VIME V": gerar_dados_base(11, 2),
            "VIME VI": gerar_dados_base(7, 1),
            "VIME VII": gerar_dados_base(13, 3),
        }
    }

    if ano not in dados or vime not in dados[ano]:
        return {
            "inadimplentes": [],
            "vazios": [],
            "ocupados": [],
            "percentual_vazios": 0,
            "percentual_ocupados": 0,
            "inadimplencia_percentual": 0
        }

    return dados[ano][vime]


def gerar_dados_base(total_apartamentos, vazios):

    ocupados = total_apartamentos - vazios

    inadimplentes_mensal = [10,11,12,13,12,14,15,14,13,12,11,12]
    vazios_mensal = [round((vazios/total_apartamentos)*100)] * 12
    ocupados_mensal = [round((ocupados/total_apartamentos)*100)] * 12

    percentual_vazios = (vazios / total_apartamentos) * 100
    percentual_ocupados = (ocupados / total_apartamentos) * 100

    return {
        "inadimplentes": inadimplentes_mensal,
        "vazios": vazios_mensal,
        "ocupados": ocupados_mensal,
        "percentual_vazios": round(percentual_vazios,2),
        "percentual_ocupados": round(percentual_ocupados,2),
        "inadimplencia_percentual": inadimplentes_mensal[-1]
    }