import mysql.connector
import traceback
import sys

cnx_data = {
    "host": "localhost",
    "user": "root",
    "database": "pathfinder",
    "password": "Bambam&xx12"
}

cnx = mysql.connector.connect(**cnx_data)

cursor = cnx.cursor()

friends_requirements = {
    "classId": 1,
    "requirementGroups": {
        1: [
            {
                "content": "Ter, no mínimo, dez anos de idade."
            },
            {
                "content": "Ser membro ativo do Clube de Desbravadores."
            },
            {
                "content": "Memorizar e explicar o Voto e a Lei do Desbravador."
            },
            {
                "content": "Ler o livro do Clube de Leitura do ano em curso."
            },
            {
                "content": "Ler o livro Vaso de Barro."
            },
            {
                "content": "Participar ativamente da classe bíblica do seu Clube."
            }
        ],
        2: [
            {
                "content": "Memorizar e demonstrar o seu conhecimento:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Criação: O que Deus criou em cada dia da Criação."
                        },
                        {
                            "content": "10 Pragas: Quais as pragas que caíram sobre o Egito."
                        },
                        {
                            "content": "12 Tribos: O nome de cada uma das 12 tribos de Israel."
                        },
                        {
                            "content": "39 livros do Antigo Testamento e demonstrar habilidade para encontrar qualquer um deles."
                        }
                    ]
                }
            },
            {
                "content": "Ler e explicar os versos abaixo:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "João 3:16"
                        },
                        {
                            "content": "Efésios 6:1-3"
                        },
                        {
                            "content": "II Timóteo 3:16"
                        },
                        {
                            "content": "Salmo 1"
                        }
                    ]
                }
            },
            {
                "content": "Leitura bíblica:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Gn 1, 2, 3, 4:1-16, 6:11-22, 7, 8, 9:1-19, 11:1-9, 12:1-10, 13, 14;18-24, 15, 17:1-8;15-22, 18:1-15, 18:16-33, 19:1-29, 21:1-21, 22:1-19, 23, 24:1-46,48, 24:52-67, 27, 28, 29, 30:25-31; 31:2-3, 17-18, 32, 33, 37, 39, 40, 41, 42, 43, 44, 45, 47, 50"
                        },
                        {
                            "content": "Êx 1, 2, 3, 4:1-17; 27-31, 5, 7, 8, 9, 10, 11, 12, 13:17-22; 14, 15:22-27; 16, 17, 18, 19, 20, 24, 32, 33, 34:1-14; 29-35, 35:4-29 e 40."
                        }
                    ]
                }
            }
        ],
        3: [
            {
                "content": "Dedicar duas horas ajudando alguém em sua comunidade, através de duas das seguintes atividades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Visitar alguém que precisa de amizade e orar com essa pessoa."
                        },
                        {
                            "content": "Oferecer alimento a alguém carente."
                        },
                        {
                            "content": "Participar de um projeto ecológico ou educativo."
                        }
                    ]
                }
            },
            {
                "content": "Escrever uma redação explicando como ser um bom cidadão no lar e na escola."
            }
        ],
        4: [
            {
                "content": "Mencionar dez qualidades de um bom amigo e apresentar quatro situações diárias onde você praticou a Regra Áurea de Mateus 7:12."
            },
            {
                "content": "Saber cantar o hino nacional de seu país e conhecer sua história. Saber o nome do autor da letra e da música do hino."
            }
        ],
        5: [
            {
                "content": "Completar uma das seguintes especialidades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Natação Principiante I"
                        },
                        {
                            "content": "Cultura física"
                        },
                        {
                            "content": "Nós e amarras"
                        },
                        {
                            "content": "Segurança básica na água"
                        }
                    ]
                }
            },
            {
                "content": "Utilizando a experiência de Daniel:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Explicar os princípios de temperança que ele defendeu ou participar em uma apresentação ou encenação sobre Daniel 1."
                        },
                        {
                            "content": "Memorizar e explicar Daniel 1:8."
                        },
                        {
                            "content": "Escrever seu compromisso pessoal de seguir um estilo de vida saudável."
                        }
                    ]
                }
            },
            {
                "content": "Aprender os princípios de uma dieta saudável e ajudar a preparar um quadro com os grupos básicos de alimentos."
            }
        ],
        6: [
            {
                "content": "Através da observação, acompanhar todo o processo de planejamento até a execução de uma caminhada de 5 quilômetros."
            }
        ],
        7: [
            {
                "content": "Completar uma das seguintes especialidades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Felinos"
                        },
                        {
                            "content": "Cães"
                        },
                        {
                            "content": "Mamíferos"
                        },
                        {
                            "content": "Sementes"
                        },
                        {
                            "content": "Aves de estimação"
                        }
                    ]
                }
            },
            {
                "content": "Aprender e demonstrar uma maneira para purificar a água e escrever um parágrafo destacando o significado de Jesus como a água da vida."
            },
            {
                "content": "Aprender e montar três diferentes tipos de barracas em locais apropriados."
            }
        ],
        8: [
            {
                "content": "Demonstrar como cuidar corretamente de uma corda. Fazer e explicar o uso prático dos seguintes nós:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Simples"
                        },
                        {
                            "content": "Cego"
                        },
                        {
                            "content": "Direito"
                        },
                        {
                            "content": "Cirurgião"
                        },
                        {
                            "content": "Lais de guia"
                        },
                        {
                            "content": "Lais de guia duplo"
                        },
                        {
                            "content": "Escota"
                        },
                        {
                            "content": "Catau"
                        },
                        {
                            "content": "Pescador"
                        },
                        {
                            "content": "Fateixa"
                        },
                        {
                            "content": "Volta do fiel"
                        },
                        {
                            "content": "Nó de gancho"
                        },
                        {
                            "content": "Volta da ribeira"
                        },
                        {
                            "content": "Ordinário"
                        }
                    ]
                }
            },
            {
                "content": "Completar a especialidade de Acampamento I"
            },
            {
                "content": "Apresentar 10 regras para uma caminhada e explicar o que fazer quando estiver perdido."
            },
            {
                "content": "Aprender os sinais para seguir uma pista. Preparar e seguir uma pista de no mínimo, 10 sinais, que também possa ser seguida por outros."
            }
        ],
        9: [
            {
                "content": "Completar uma especialidade na área de Artes e habilidades manuais."
            }
        ],
        10: [
            {
                "content": "Memorizar, cantar ou tocar o Hino dos Desbravadores e conhecer a história do hino."
            },
            {
                "content": "Em consulta com seu líder, escolher um dos seguintes personagens do Antigo Testamento e conversar com seu grupo sobre o amor e cuidado de Deus e o livramento demonstrado na vida do personagem escolhido.",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "José"
                        },
                        {
                            "content": "Jonas"
                        },
                        {
                            "content": "Ester"
                        },
                        {
                            "content": "Rute"
                        }
                    ]
                }
            },
            {
                "content": "Levar pelo menos dois amigos não adventistas à Escola Sabatina ou ao Clube de Desbravadores."
            },
            {
                "content": " Conhecer os princípios de higiene, de boas maneiras à mesa e como se comportar diante de pessoas que tenham diferentes idades. Demonstrar e explicar como estas boas maneiras podem ser úteis nas reuniões e acampamentos do clube."
            },
            {
                "content": "Fazer a especialidade de Arte de acampar."
            },
            {
                "content": "Conhecer e identificar 10 flores silvestres e 10 insetos de sua região."
            },
            {
                "content": "Começar uma fogueira com apenas um fósforo, usando materiais naturais, e mantê-la acesa."
            },
            {
                "content": "Usar corretamente uma faca, facão ou uma machadinha e conhecer dez regras para usá-los com segurança."
            },
            {
                "content": "Escolher e completar uma especialidade em uma das áreas abaixo:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Atividades missionárias e comunitárias"
                        },
                        {
                            "content": "Atividades agrícolas e afins"
                        }
                    ]
                }
            }
        ]
    }
}

companion_requirements = {
    "classId": 2,
    "requirementGroups": {
        1: [
            {
                "content": "Ter, no mínimo, 11 anos de idade."
            },
            {
                "content": "Ser membro ativo do Clube de Desbravadores."
            },
            {
                "content": "Ilustrar de forma criativa o significado do Voto do Desbravador."
            },
            {
                "content": "Ler o livro do Clube de Leitura do ano em curso e escrever um parágrafo sobre o que mais lhe chamou atenção ou considerou importante."
            },
            {
                "content": "Ler o livro Caminho a Cristo."
            },
            {
                "content": "Participar ativamente da classe bíblica do seu clube."
            }
        ],
        2: [
            {
                "content": "Memorizar e demonstrar o seu conhecimento:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "10 Mandamentos: A Lei de Deus dada a Moisés."
                        },
                        {
                            "content": "27 livros do Novo Testamento e demonstrar habilidade para encontrar qualquer um deles."
                        }
                    ]
                }
            },
            {
                "content": "Memorizar e recitar os versos abaixo:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Isa. 41:9-10"
                        },
                        {
                            "content": "Heb. 13:5"
                        },
                        {
                            "content": "Prov. 22:6"
                        },
                        {
                            "content": "I João 1:9"
                        },
                        {
                            "content": "Salmo 8"
                        }
                    ]
                }
            },
            {
                "content": "Leitura bíblica:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Lv 11"
                        },
                        {
                            "content": "Nm 9:15-23, 11, 12, 13, 14:1-38, 16, 17, 20:1-13; 22-29, 21:4-9, 22, 23; 24:1-10"
                        },
                        {
                            "content": "Dt 1:1-17; 4:1-8, 32:1-43, 33, 34"
                        },
                        {
                            "content": "Js 1, 2, 3, 4, 5:10; 6, 7, 9, 24:1-15; 29"
                        },
                        {
                            "content": "Jz 6, 7, 13:1-18; 14, 15, 16"
                        },
                        {
                            "content": "Rt 1, 2, 3, 4"
                        },
                        {
                            "content": "1 Sm 1, 2, 3, 4, 5, 6, 8, 9, 10, 11:12-15, 12, 13, 15, 16, 17, 18:1-19, 20, 21:1-7; 22, 24, 25, 26, 31"
                        },
                        {
                            "content": "2 Sm 1, 5, 6, 7, 9, 11; 12:1-25, 15, 18"
                        }
                    ]
                }
            },
            {
                "content": "Em consulta com o seu conselheiro, escolher um dos seguintes temas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Uma parábola de Jesus"
                        },
                        {
                            "content": "Um milagre de Jesus"
                        },
                        {
                            "content": "O Sermão da Montanha"
                        },
                        {
                            "content": "Um sermão sobre a segunda vinda de Cristo"
                        }
                    ]
                }
            },
            {
                "content": "Escolher um item abaixo para demonstrar seu conhecimento sobre o tema escolhido:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Troca de ideias com o seu conselheiro"
                        },
                        {
                            "content": "Atividade que integre todo o grupo"
                        },
                        {
                            "content": "Redação"
                        }
                    ]
                }
            }
        ],
        3: [
            {
                "content": "Planejar e dedicar pelo menos duas horas servindo sua comunidade e demonstrando companheirismo a alguém, de maneira prática."
            },
            {
                "content": "Participar de um projeto que beneficiará sua comunidade ou igreja."
            }
        ],
        4: [
            {
                "content": "Conversar com seu conselheiro ou unidade sobre como respeitar pessoas de diferentes culturas, raça e sexo."
            }
        ],
        5: [
            {
                "content": "Memorizar e explicar I Coríntios 9:24-27."
            },
            {
                "content": "Conversar com seu líder sobre a aptidão física e os exercícios físicos regulares que se relacionam com uma vida saudável."
            },
            {
                "content": "Aprender sobre os prejuízos que o cigarro causa à saúde e escrever seu compromisso de não fazer uso do fumo."
            },
            {
                "content": "Completar uma das seguintes especialidades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Natação principiante II"
                        },
                        {
                            "content": "Acampamento II"
                        }
                    ]
                }
            }
        ],
        6: [
            {
                "content": "Dirigir ou colaborar em uma meditação criativa para sua unidade ou Clube."
            },
            {
                "content": "Ajudar no planejamento de uma excursão ou acampamento com sua unidade ou clube, envolvendo pelo menos um pernoite."
            }
        ],
        7: [
            {
                "content": "Participar de jogos na natureza ou caminhada ecológica, pelo período de uma hora."
            },
            {
                "content": "Completar duas das seguintes especialidades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Anfíbios"
                        },
                        {
                            "content": "Aves"
                        },
                        {
                            "content": "Aves domésticas"
                        },
                        {
                            "content": "Pecuária"
                        },
                        {
                            "content": "Répteis"
                        },
                        {
                            "content": "Moluscos"
                        },
                        {
                            "content": "Árvores"
                        },
                        {
                            "content": "Arbustos"
                        }
                    ]
                }
            },
            {
                "content": "Recapitular o estudo da Criação e fazer um diário por sete dias registrando suas observações do que foi criado em cada dia correspondente."
            }
        ],
        8: [
            {
                "content": "Descobrir os pontos cardeais sem a ajuda de uma bússola e desenhar a Rosa dos Ventos."
            },
            {
                "content": "Participar de um acampamento de final de semana e fazer um relatório destacando o que mais lhe impressionou positivamente."
            },
            {
                "content": "Aprender ou recapitular os seguintes nós:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Oito"
                        },
                        {
                            "content": "Volta do salteador"
                        },
                        {
                            "content": "Duplo"
                        },
                        {
                            "content": "Caminhoneiro"
                        },
                        {
                            "content": "Direito"
                        },
                        {
                            "content": "Volta do Fiel"
                        },
                        {
                            "content": "Escota"
                        },
                        {
                            "content": "Lais de Guia"
                        },
                        {
                            "content": "Simples"
                        }
                    ]
                }
            }
        ],
        9: [
            {
                "content": "Completar uma especialidade não realizada anteriormente na seção de Artes e habilidades manuais."
            }
        ],
        10: [
            {
                "content": "Aprender e demonstrar a composição, significado e uso correto da Bandeira Nacional."
            },
            {
                "content": "Ler a primeira visão de Ellen White e discutir como Deus usa os profetas para apresentar Sua mensagem à igreja (ver Primeiros Escritos, p. 13 a 20)."
            },
            {
                "content": "Participar de uma atividade missionária ou comunitária, envolvendo também um amigo."
            },
            {
                "content": "Conversar com seu conselheiro ou unidade sobre como demonstrar respeito pelos seus pais ou responsáveis e fazer uma lista mostrando como cuidam de você."
            },
            {
                "content": "Participar de uma caminhada de 6 quilômetros, preparando, ao final, um relatório de uma página."
            },
            {
                "content": "Escolher um dos seguintes itens:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Assistir a um Curso como deixar de fumar"
                        },
                        {
                            "content": "Assistir a dois filmes sobre saúde"
                        },
                        {
                            "content": "Elaborar um cartaz sobre o prejuízo das drogas"
                        },
                        {
                            "content": "Ajudar a preparar material para uma exposição ou passeata sobre saúde"
                        },
                        {
                            "content": "Pesquisar na internet informações sobre saúde e escrever uma página sobre os resultados encontrados"
                        }
                    ]
                }
            },
            {
                "content": "Identificar e descrever 12 aves nativas e 12 árvores nativas."
            },
            {
                "content": "Participar de uma das seguintes cerimônias e sugerir ideias criativas e como realizá-las.",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Investidura"
                        },
                        {
                            "content": "Admissão em lenço"
                        },
                        {
                            "content": "Dia Mundial do Desbravador"
                        }
                    ]
                }
            },
            {
                "content": "Preparar uma refeição em uma fogueira durante um acampamento do clube ou unidade."
            },
            {
                "content": "Preparar um quadro com 15 nós diferentes."
            },
            {
                "content": "Preparar um quadro com 15 nós diferentes."
            },
            {
                "content": "Completar uma especialidade não realizada anteriormente.",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Habilidades domésticas"
                        },
                        {
                            "content": "Ciência e saúde"
                        },
                        {
                            "content": "Atividades missionárias e comunitárias"
                        },
                        {
                            "content": "Atividades agrícolas e afins"
                        }
                    ]
                }
            }
        ]
    }
}

researcher_requirements = {
    "classId": 3,
    "requirementGroups": {
        1: [
            {
                "content": "Ter, no mínimo, 12 anos de idade."
            },
            {
                "content": "Ser membro ativo do Clube de Desbravadores."
            },
            {
                "content": "Demonstrar sua compreensão do significado da Lei do Desbravador através de uma das seguintes atividades.",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Representação"
                        },
                        {
                            "content": "Debate"
                        },
                        {
                            "content": "Redação"
                        }
                    ]
                }
            },
            {
                "content": "Ler o livro do Clube de Leitura do ano em curso e escrever dois parágrafos sobre o que mais lhe chamou atenção ou considerou importante."
            },
            {
                "content": "Ler o livro Além da Magia."
            },
            {
                "content": "Participar ativamente da classe bíblica do seu clube."
            }
        ],
        2: [
            {
                "content": "Memorizar e demonstrar o seu conhecimento:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Levítico 11: Quais as regras dos alimentos considerados comestíveis e não comestíveis."
                        }
                    ]
                }
            },
            {
                "content": "Ler e explicar os versos abaixo:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Ecles. 12:13-14"
                        },
                        {
                            "content": "Rom. 6:23"
                        },
                        {
                            "content": "Apoc. 1:3"
                        },
                        {
                            "content": "Isa. 43:1-2"
                        },
                        {
                            "content": "Salmo 51:10"
                        },
                        {
                            "content": "Salmo 16"
                        }
                    ]
                }
            },
            {
                "content": "Leitura bíblica:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "1 Rs 1:28-53, 3, 4:20-34, 5, 6, 8:12-60, 10, 11:6-43, 12, 16:29-33, 17:1-7, 17:8-24, 18, 19, 21"
                        },
                        {
                            "content": "2 Rs 2, 4:1-7, 4:8-41, 5, 6:1-23, 6:24-33, 7, 20, 22, 23:36-37, 24, 25:1-7"
                        },
                        {
                            "content": "2 Cr 24:1-14, 36"
                        },
                        {
                            "content": "Ed 1, 3, 6:14-15"
                        },
                        {
                            "content": "Ne 1, 2, 4, 8"
                        },
                        {
                            "content": "Ester 1, 2, 3, 4, 5, 6, 7, 8"
                        },
                        {
                            "content": "Jó 1, 2, 42"
                        },
                        {
                            "content": "Sl 1, 15, 19, 23, 24, 27, 37, 39, 42, 46, 67, 90, 91, 92, 97, 98, 100, 117, 119:1-176, 121, 125, 150"
                        },
                        {
                            "content": "Pv 1, 3, 4, 10, 15, 20, 25"
                        },
                        {
                            "content": "Ec 1"
                        }
                    ]
                }
            },
            {
                "content": "Conversar com seu líder e escolher uma das seguintes histórias:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "João 3 - Nicodemos"
                        },
                        {
                            "content": "João 4 - A mulher samaritana"
                        },
                        {
                            "content": "Lucas 10 - O bom samaritano"
                        },
                        {
                            "content": "Lucas 15 - O filho pródigo"
                        },
                        {
                            "content": "Lucas 19 - Zaqueu"
                        }
                    ]
                }
            },
            {
                "content": "Através da história escolhida, demonstrar sua compreensão em como Jesus salva as pessoas, usando um dos métodos abaixo.",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Conversar em grupo com a participação de seu líder"
                        },
                        {
                            "content": "Apresentar uma mensagem em uma reunião do Clube"
                        },
                        {
                            "content": "Fazer uma série de cartazes ou uma maquete"
                        },
                        {
                            "content": "Escrever uma poesia ou hino"
                        }
                    ]
                }
            }
        ],
        3: [
            {
                "content": "Conhecer os projetos comunitários desenvolvidos em sua cidade e participar em pelo menos um deles com sua unidade ou Clube."
            },
            {
                "content": "Participar em três atividades missionárias da igreja."
            }
        ],
        4: [
            {
                "content": " Participar de um debate ou representação sobre a pressão de grupo e identificar a influência que isto exerce sobre suas decisões."
            },
            {
                "content": "Visitar um órgão público de sua cidade ou bairro e descobrir de que maneiras o clube pode ser útil à sua comunidade."
            }
        ],
        5: [
            {
                "content": "Escolher uma das atividades abaixo e escrever um texto pessoal para um estilo de vida livre do álcool:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Participar de uma discussão em classe sobre os efeitos do álcool no organismo."
                        },
                        {
                            "content": "Assistir a um vídeo sobre o efeito do álcool ou outras drogas no corpo humano e conversar sobre o assunto."
                        }
                    ]
                }
            }
        ],
        6: [
            {
                "content": "Dirigir uma cerimônia de abertura da reunião semanal em seu clube ou um programa de Escola Sabatina."
            },
            {
                "content": "Ajudar a organizar a classe bíblica do seu clube."
            }
        ],
        7: [
            {
                "content": "Identificar a estrela Alfa da constelação do Centauro e a constelação de Órion. Conhecer o significado espiritual de Órion, como descrito no livro Primeiros Escritos, de Ellen White, pág. 41."
            },
            {
                "content": "Completar uma das especialidades a seguir:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Astronomia"
                        },
                        {
                            "content": "Cactos"
                        },
                        {
                            "content": "Climatologia"
                        },
                        {
                            "content": "Flores"
                        },
                        {
                            "content": "Rastreio de animais"
                        }
                    ]
                }
            }
        ],
        8: [
            {
                "content": "Apresentar seis segredos para um bom acampamento. Participar de um acampamento de final de semana, planejando e cozinhando duas refeições."
            },
            {
                "content": "Completar as seguintes especialidades.",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Acampamento III"
                        },
                        {
                            "content": "Primeiros socorros - básico"
                        }
                    ]
                }
            },
            {
                "content": "Aprender a usar uma bússola ou um GPS (urbano ou campo), e demonstrar sua habilidade encontrando endereços em uma zona urbana."
            }
        ],
        9: [
            {
                "content": "Completar uma especialidade, não realizada anteriormente, em Artes e habilidades manuais."
            }
        ],
        10: [
            {
                "content": "Conhecer e saber usar de forma adequada a bandeira dos Desbravadores e o bandeirim de unidade e os comandos de ordem unida."
            },
            {
                "content": "Ler a história de J. N. Andrews ou um pioneiro de seu país e discutir a importância do trabalho de missionários, e por que Cristo ordenou a Grande Comissão (Mateus 28:18-20)."
            },
            {
                "content": "Convidar uma pessoa para assistir um dos seguintes programas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Clube de Desbravadores"
                        },
                        {
                            "content": "Classe bíblica"
                        },
                        {
                            "content": "Pequenos grupos"
                        }
                    ]
                }
            },
            {
                "content": "Fazer uma das seguintes especialidades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Asseio e cortesia cristã"
                        },
                        {
                            "content": "Vida familiar"
                        }
                    ]
                }
            },
            {
                "content": "Participar de uma caminhada de 10 quilômetros e fazer uma lista dos equipamentos necessários, incluindo a roupa e o calçado que devem ser usados."
            },
            {
                "content": "Participar na organização de um dos eventos especiais do Clube:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "investidura"
                        },
                        {
                            "content": "Admissão em lenço"
                        },
                        {
                            "content": "Dia Mundial do Desbravador"
                        }
                    ]
                }
            },
            {
                "content": "Identificar seis pegadas de animais ou aves. Fazer um modelo em gesso, massa de modelar ou biscuit de três dessas pegadas."
            },
            {
                "content": "Aprender a fazer as quatro amarras básicas e construir um móvel de acampamento."
            },
            {
                "content": "Planejar um cardápio vegetariano para sua unidade, para um acampamento de 3 dias e apresentar ao seu instrutor."
            },
            {
                "content": "Enviar e receber uma mensagem através das formas de comunicação abaixo:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Alfabeto com semáforos"
                        },
                        {
                            "content": "Código Morse, com lanterna"
                        },
                        {
                            "content": "Alfabeto LIBRAS (língua de sinais)"
                        },
                        {
                            "content": "Alfabeto Braile"
                        }
                    ]
                }
            },
            {
                "content": "Completar duas especialidades, não realizadas anteriormente, em uma das áreas abaixo:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Habilidades domésticas"
                        },
                        {
                            "content": "Ciência e saúde"
                        },
                        {
                            "content": "Atividades missionárias e comunitárias"
                        },
                        {
                            "content": "Atividades agrícolas e afins"
                        }
                    ]
                }
            }
        ]
    }
}

pioneer_requirements = {
    "classId": 4,
    "requirementGroups": {
        1: [
            {
                "content": "Ter, no mínimo, 13 anos de idade."
            },
            {
                "content": "Ser membro ativo do Clube de Desbravadores."
            },
            {
                "content": "Memorizar e entender o Alvo e o Lema JA."
            },
            {
                "content": "Ler o livro do Clube de Leitura do ano em curso e resumi-lo em uma página."
            },
            {
                "content": "Ler o livro A história da vida."
            }
        ],
        2: [
            {
                "content": "Memorizar e demonstrar o seu conhecimento:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Bem-Aventuranças: O Sermão da Montanha."
                        }
                    ]
                }
            },
            {
                "content": "Ler e explicar os versos abaixo:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Isa. 26:3"
                        },
                        {
                            "content": "Rom. 12:12"
                        },
                        {
                            "content": "João 14:1-3"
                        },
                        {
                            "content": "Sal. 37:5"
                        },
                        {
                            "content": "Filip. 3:12-14"
                        },
                        {
                            "content": "Salmo 23"
                        },
                        {
                            "content": "I Sam. 15:22"
                        }
                    ]
                }
            },
            {
                "content": "Conversar em seu clube ou unidade sobre:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "O que é o cristianismo"
                        },
                        {
                            "content": "Quais são as características de um verdadeiro discípulo"
                        },
                        {
                            "content": "O que fazer para ser um cristão verdadeiro"
                        }
                    ]
                }
            },
            {
                "content": "Participar de um estudo especial sobre a inspiração da Bíblia, com a ajuda de um pastor, trabalhando os conceitos de inspiração, revelação e iluminação."
            },
            {
                "content": "Convidar três ou mais pessoas para assistirem a uma classe bíblica ou pequeno grupo."
            },
            {
                "content": "Leitura Bíblica:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Ec 3, 5, 7, 11 e 12"
                        },
                        {
                            "content": "Is 5, 11, 26:1-12, 35, 40, 43, 52:13-15, 53, 58, 60, 61"
                        },
                        {
                            "content": "Jr 9:23-26, 10:1-16, 18:1-6, 26, 36, 52:1-11"
                        },
                        {
                            "content": "Dn 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12"
                        },
                        {
                            "content": "Jl 2:12-31"
                        },
                        {
                            "content": "Am 7:10-16, 8:4-11"
                        },
                        {
                            "content": "Jn 1, 2, 3 e 4"
                        },
                        {
                            "content": "Mq 4"
                        },
                        {
                            "content": "Ag 2"
                        },
                        {
                            "content": "Zc 4"
                        },
                        {
                            "content": "Ml 3 e 4"
                        },
                        {
                            "content": "Mt 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23"
                        }
                    ]
                }
            }
        ],
        3: [
            {
                "content": "Participar em dois projetos missionários definidos por seu Clube."
            },
            {
                "content": "Trabalhar em um projeto comunitário de sua igreja, escola ou comunidade."
            }
        ],
        4: [
            {
                "content": "Participar de um debate e fazer uma avaliação pessoal sobre suas atitudes em dois dos seguintes temas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Autoestima"
                        },
                        {
                            "content": "Amizade"
                        },
                        {
                            "content": "Relacionamentos"
                        },
                        {
                            "content": "Otimismo e pessimismo"
                        }
                    ]
                }
            }
        ],
        5: [
            {
                "content": "Preparar um programa pessoal de exercícios físicos diários e conversar com seu líder ou conselheiro sobre os princípios de aptidão física. Fazer e assinar um compromisso pessoal de realizar exercícios físicos regularmente."
            },
            {
                "content": "Discutir as vantagens do estilo de vida adventista de acordo com o que a Bíblia ensina."
            }
        ],
        6: [
            {
                "content": "Assistir a um seminário ou treinamento, oferecido pela sua igreja ou distrito nos departamentos abaixo:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Ministério Pessoal"
                        },
                        {
                            "content": "Evangelismo"
                        }
                    ]
                }
            },
            {
                "content": "Participar de uma atividade social de sua igreja."
            }
        ],
        7: [
            {
                "content": "Estudar a história do dilúvio e estudar o processo de fossilização."
            },
            {
                "content": "Completar uma especialidade, não realizada anteriormente, em Estudo da natureza."
            }
        ],
        8: [
            {
                "content": "Fazer um fogo refletor e demonstrar seu uso."
            },
            {
                "content": "Participar de um acampamento de final de semana, arrumando de forma apropriada sua bolsa ou mochila com o equipamento pessoal necessário."
            },
            {
                "content": "Completar a especialidade de Resgate básico."
            }
        ],
        9: [
            {
                "content": "Completar uma especialidade não realizada anteriormente em uma das seguintes áreas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Atividades missionárias e comunitárias"
                        },
                        {
                            "content": "Atividades profissionais"
                        },
                        {
                            "content": "Atividades agrícolas e afins"
                        }
                    ]
                }
            }
        ],
        10: [
            {
                "content": "Completar a especialidade de Cidadania cristã, caso não tenha sido realizada anteriormente."
            },
            {
                "content": "Dar dois estudos bíblicos a uma pessoa não batizada na Igreja Adventista."
            },
            {
                "content": "Encenar a história do bom samaritano, demonstrando como ajudar as pessoas e auxiliar de forma prática três pessoas ou mais."
            },
            {
                "content": "Participar de uma das seguintes atividades, apresentando ao final um relatório escrito contendo no mínimo duas páginas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Caminhar 10 quilômetros"
                        },
                        {
                            "content": "Cavalgar 2 quilômetros"
                        },
                        {
                            "content": "Viajar de canoa durante 2 horas"
                        },
                        {
                            "content": "Praticar 15 quilômetros de ciclismo"
                        },
                        {
                            "content": "Nadar 200 metros"
                        },
                        {
                            "content": "Correr 1500m"
                        },
                        {
                            "content": "Rodar 2 km de patins ou roller"
                        }
                    ]
                }
            },
            {
                "content": "Completar a especialidade de Mapa e bússola."
            },
            {
                "content": "Demonstrar habilidade no uso correto de uma machadinha."
            },
            {
                "content": "Ser capaz de acender uma fogueira em dia de chuva, saber como conseguir lenha seca e manter o fogo aceso."
            },
            {
                "content": "Completar um dos seguintes itens:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Pesquisar e identificar dez variedades de plantas silvestres comestíveis."
                        },
                        {
                            "content": "Ser capaz de enviar e receber 35 letras por minuto pelo código semafórico."
                        },
                        {
                            "content": "Ser capaz de enviar e receber 35 letras por minuto através do código náutico, usando o código internacional."
                        },
                        {
                            "content": "Ser capaz de apresentar e entender Mateus 24 em LIBRAS (língua de sinais)."
                        },
                        {
                            "content": "Preparar o salmo 23 em braile."
                        }
                    ]
                }
            },
            {
                "content": "Completar uma especialidade, não realizada anteriormente, em Atividades recreativas."
            },
            {
                "content": "Pesquisar e identificar, através de fotografia, exposição ou ao vivo, um dos seguintes itens:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "25 folhas de árvores"
                        },
                        {
                            "content": "25 rochas e minerais"
                        },
                        {
                            "content": "25 flores silvestres"
                        },
                        {
                            "content": "25 borboletas e mariposas"
                        },
                        {
                            "content": "25 conchas"
                        }
                    ]
                }
            },
            {
                "content": "Completar a especialidade de Fogueiras e cozinha ao ar livre."
            }
        ]
    }
}

hiker_requirements = {
    "classId": 5,
    "requirementGroups": {
        1: [
            {
                "content": "Ter, no mínimo, 14 anos de idade."
            },
            {
                "content": "Ser membro ativo do Clube de Desbravadores."
            },
            {
                "content": "Memorizar e explicar o significado do Objetivo JA."
            },
            {
                "content": "Ler o livro do Clube de Leitura do ano em curso e resumi-lo em uma página."
            },
            {
                "content": "Ler o livro Nos bastidores da mídia."
            }
        ],
        2: [
            {
                "content": "Memorizar e demonstrar o seu conhecimento:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "12 Apóstolos: O nome dos 12 apóstolos de Cristo."
                        },
                        {
                            "content": "O Fruto do Espírito: A relação de adjetivos do caráter do cristão."
                        }
                    ]
                }
            },
            {
                "content": "Memorizar e recitar os versos abaixo:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Rom. 12:12"
                        },
                        {
                            "content": "Apoc. 21:1-3"
                        },
                        {
                            "content": "II Ped. 1:20-21"
                        },
                        {
                            "content": "I João 2:14"
                        },
                        {
                            "content": "II Cro. 20:20"
                        },
                        {
                            "content": "Salmo 46"
                        }
                    ]
                }
            },
            {
                "content": "Estudar e entender a pessoa do Espírito Santo, como Ele se relaciona, e qual o Seu papel no crescimento espiritual de cada ser humano."
            },
            {
                "content": "Estude, com a sua unidade, os eventos finais e a segunda vinda de Cristo."
            },
            {
                "content": "Através do estudo da Bíblia, descobrir o verdadeiro significado da observância do sábado."
            },
            {
                "content": "Leitura bíblica",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "Mt 24, 25, 26:1-35, 26:36-75, 27:1-31, 27:32-56, 27:57-66, 28"
                        },
                        {
                            "content": "Mc 7, 9, 10, 11, 12, 16"
                        },
                        {
                            "content": "Lc 1:4-25, 1:26-66, 2:21-38, 2:39-52, 7:18-28, 8, 10:1-37, 10:38-42, 11:1-13, 12, 13, 14, 15, 16:1-17, 17, 18, 19, 21, 22, 23, 24"
                        },
                        {
                            "content": "Jo 1, 2, 3, 4, 5, 6:1-21, 6:22-71, 8:1-38, 9, 10, 11:1-46, 12, 13, 14, 15, 17, 18, 19, 20, 21"
                        },
                        {
                            "content": "At 1, 2, 3, 4, 5, 6, 7, 8"
                        }
                    ]
                }
            }
        ],
        3: [
            {
                "content": "Convidar um amigo para participar de uma atividade social de sua igreja ou da Associação/Missão."
            },
            {
                "content": "Participar de um projeto comunitário desde o planejamento, organização até a execução."
            },
            {
                "content": "Discutir como os jovens adventistas devem se relacionar com as pessoas nas diferentes situações do dia a dia, tais como:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Vizinhança"
                        },
                        {
                            "content": "Escola"
                        },
                        {
                            "content": "Atividades sociais"
                        },
                        {
                            "content": "Atividades recreativas"
                        }
                    ]
                }
            }
        ],
        4: [
            {
                "content": "Através de uma conversa em grupo ou avaliação pessoal, examinar suas atitudes em dois dos seguintes temas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Autoestima."
                        },
                        {
                            "content": "Relacionamento familiar."
                        },
                        {
                            "content": "Finanças pessoais."
                        },
                        {
                            "content": "Pressão de grupo."
                        }
                    ]
                }
            },
            {
                "content": "Preparar uma lista contendo cinco sugestões de atividades recreativas para ajudar pessoas com necessidades especificas e colaborar na organização de uma atividade para essas pessoas."
            }
        ],
        5: [
            {
                "content": "Completar a especialidade de Temperança."
            }
        ],
        6: [
            {
                "content": "Preparar um organograma da igreja local e relacionar as funções dos departamentos."
            },
            {
                "content": "Participar de dois programas envolvendo diferentes departamentos da igreja local."
            },
            {
                "content": "Completar a especialidade de Aventuras com Cristo."
            }
        ],
        7: [
            {
                "content": "Recapitular a história de Nicodemos e relacioná-la com o ciclo de vida da lagarta ou borboleta, acrescentando um significado espiritual."
            },
            {
                "content": "Completar uma especialidade em Estudo da natureza, não realizada anteriormente."
            }
        ],
        8: [
            {
                "content": "Com um grupo de, no mínimo, quatro pessoas e com a presença de um conselheiro adulto e experiente, andar pelo menos 20 quilômetros numa área rural ou deserta, incluindo uma noite ao ar livre ou em barraca. Planejar a expedição em detalhes antes da saída. Durante a caminhada, efetuar anotações sobre o terreno, flora e fauna observados. Depois, usando as anotações, participar de uma discussão em grupo, dirigida por seu conselheiro."
            },
            {
                "content": "Completar a especialidade de Pioneirias."
            }
        ],
        9: [
            {
                "content": "Completar uma especialidade não realizada anteriormente em uma das seguintes áreas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Completar uma especialidade não realizada anteriormente em uma das seguintes áreas:"
                        },
                        {
                            "content": "Atividades agrícolas e afins"
                        },
                        {
                            "content": "Ciência e saúde"
                        },
                        {
                            "content": "Habilidades domésticas"
                        }
                    ]
                }
            }
        ],
        10: [
            {
                "content": "Fazer uma apresentação escrita ou falada sobre o respeito que devemos ter com a Lei de Deus e as autoridades civis, enumerando 10 princípios de comportamento moral."
            },
            {
                "content": "Acompanhar seu pastor ou ancião numa visita missionária ou estudo bíblico."
            },
            {
                "content": "Completar a especialidade de Testemunho juvenil."
            },
            {
                "content": "Apresentar cinco atividades na natureza, para serem realizadas no sábado à tarde."
            },
            {
                "content": "Com sua unidade, construir cinco móveis de acampamento e um portal para o clube."
            },
            {
                "content": "Sob a supervisão de seu líder ou conselheiro, conversar em sua unidade ou clube sobre um dos seguintes temas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Modéstia cristã."
                        },
                        {
                            "content": "Recreação."
                        },
                        {
                            "content": "Saúde."
                        },
                        {
                            "content": "Observância do sábado."
                        }
                    ]
                }
            },
            {
                "content": "Demonstrar conhecimento para encontrar alimentos, através de plantas silvestres de sua região e saber diferenciá-las de plantas tóxicas/venenosas."
            },
            {
                "content": "Demonstrar conhecimento quanto aos procedimentos necessários em caso de ferimentos por diferentes animais peçonhentos e não peçonhentos."
            },
            {
                "content": "Demonstrar técnicas para percorrer trilhas em diferentes tipos de terrenos, como: desertos, florestas, pântanos e rios."
            },
            {
                "content": "Completar a especialidade de Ordem unida, caso não tenha sido realizada anteriormente."
            },
            {
                "content": "Completar a especialidade de Vida silvestre."
            }
        ]
    }
}

guide_requirements = {
    "classId": 6,
    "requirementGroups": {
        1: [
            {
                "content": "Ter, no mínimo, 15 anos de idade."
            },
            {
                "content": "Ser membro ativo do Clube de Desbravadores."
            },
            {
                "content": "Memorizar e explicar o Voto de Fidelidade à Bíblia."
            },
            {
                "content": "Ler o livro do Clube de Leitura do ano em curso e resumi-lo em uma página"
            },
            {
                "content": "Ler o livro Nossa Herança."
            }
        ],
        2: [
            {
                "content": "Memorizar e demonstrar o seu conhecimento:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "As 3 Mensagens Angélicas: Reveladas em Apocalipse 14:6-12."
                        },
                        {
                            "content": "7 Igrejas: O nome das igrejas do Apocalipse."
                        },
                        {
                            "content": "Pedras preciosas: Quais as pedras preciosas dos 12 fundamentos da cidade santa – a nova Jerusalém."
                        }
                    ]
                }
            },
            {
                "content": "Ler e explicar os versos abaixo:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "I Cor. 13"
                        },
                        {
                            "content": "II Cron. 7:14"
                        },
                        {
                            "content": "Apoc. 22:18-20"
                        },
                        {
                            "content": "II Tim. 4:6-7"
                        },
                        {
                            "content": "Rom. 8:38-39"
                        },
                        {
                            "content": "Mateus 6:33-34"
                        }
                    ]
                }
            },
            {
                "content": "Descrever os dons espirituais mencionados nos escritos de Paulo (Coríntios, Efésios, Filipenses) e para que a igreja recebe estes dons."
            },
            {
                "content": "Estudar a estrutura e serviço do santuário no Antigo Testamento e relacionar com o ministério pessoal de Jesus e a cruz."
            },
            {
                "content": "Ler e resumir três histórias de pioneiros adventistas. Contar estas histórias na reunião do Clube, no culto JA ou na escola sabatina."
            },
            {
                "content": "Leitura bíblica:",
                "subRequirements": {
                    "type": 2,
                    "subRequirements": [
                        {
                            "content": "At 9:1-31, 9:32-43, 10, 11, 12, 13, 14, 16, 17:1-15, 17:16-34, 18, 19:1-22, 19:23-41, 20, 21:17-40, 22:1-16, 23, 24, 25, 26, 27, 28"
                        },
                        {
                            "content": "Rm 12, 13, 14"
                        },
                        {
                            "content": "1 Co 13"
                        },
                        {
                            "content": "2 Co 5:11-21, Co 11:16-33, 12:1-10"
                        },
                        {
                            "content": "Gl 5:16-26, 6:1-10"
                        },
                        {
                            "content": "Ef 5:1-21, 6"
                        },
                        {
                            "content": "Fp 4"
                        },
                        {
                            "content": "Cl 3"
                        },
                        {
                            "content": "1 Ts 4:13-18, 5"
                        },
                        {
                            "content": "2 Ts 2, 3"
                        },
                        {
                            "content": "1 Tm 4:6-16, Tm 5:1-16, 6:11-21"
                        },
                        {
                            "content": "2 Tm 2, 3"
                        },
                        {
                            "content": "Fm"
                        },
                        {
                            "content": "Hb 11"
                        },
                        {
                            "content": "Tg 1, 3, 5:7-20"
                        },
                        {
                            "content": "1 Pe 1, 5:1-11"
                        },
                        {
                            "content": "2 Pe 3"
                        },
                        {
                            "content": "1 Jo 2, 3, 4, 5"
                        },
                        {
                            "content": "Jd 1:17-25"
                        },
                        {
                            "content": "Ap 1, 2, 3, 7:9-17, 12, 13, 14, 19, 20, 21"
                        }
                    ]
                }
            }
        ],
        3: [
            {
                "content": "Ajudar a organizar e participar de uma das seguintes atividades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Fazer uma visita de cortesia a uma pessoa doente."
                        },
                        {
                            "content": "Adotar uma pessoa ou família em necessidade."
                        },
                        {
                            "content": "Um projeto de sua escolha aprovado por seu líder."
                        }
                    ]
                }
            },
            {
                "content": "Discutir com sua unidade os métodos de evangelismo pessoal e colocar alguns princípios em prática."
            }
        ],
        4: [
            {
                "content": "Assistir a uma palestra ou aula e examinar suas atitudes em relação a dois dos seguintes temas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "A importância da escolha profissional."
                        },
                        {
                            "content": "Como se relacionar com os pais."
                        },
                        {
                            "content": "A escolha da pessoa certa para namorar."
                        },
                        {
                            "content": "O plano de Deus para o sexo."
                        }
                    ]
                }
            }
        ],
        5: [
            {
                "content": "Fazer uma apresentação, para os alunos do ensino fundamental, sobre os oito remédios naturais dados por Deus."
            },
            {
                "content": "Completar uma das seguintes atividades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Escrever uma poesia ou artigo sobre saúde para ser divulgado em uma revista, boletim ou jornal da igreja."
                        },
                        {
                            "content": "Individualmente ou em grupo, organizar e participar de uma corrida ou atividade similar e apresentar com antecedência um programa de treinamento físico para este evento."
                        },
                        {
                            "content": "Ler as páginas 102-125 do livro Temperança, de Ellen White, e apresentar em uma página ou mais, 10 textos selecionados da leitura."
                        },
                        {
                            "content": "Completar a especialidade de Nutrição ou liderar um grupo para a especialidade de Cultura física."
                        }
                    ]
                }
            }
        ],
        6: [
            {
                "content": "Preparar um organograma da estrutura administrativa da Igreja Adventista em sua Divisão."
            },
            {
                "content": "Participar em um dos itens abaixo:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Curso para conselheiros"
                        },
                        {
                            "content": "Convenção de liderança da Associação/Missão"
                        },
                        {
                            "content": "6 reuniões de diretoria do seu Clube"
                        }
                    ]
                }
            },
            {
                "content": "Planejar e ensinar, no mínimo, dois requisitos de uma especialidade para um grupo ou unidade de desbravadores."
            }
        ],
        7: [
            {
                "content": "Ler o capítulo 7 do livro O Desejado de Todas as Nações sobre a infância de Jesus. Apresentar para um grupo, clube ou unidade as lições encontradas, demonstrando a importância que o estudo da natureza exerceu na educação e ministério de Jesus."
            },
            {
                "content": "Completar uma das seguintes especialidades:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Ecologia."
                        },
                        {
                            "content": "Conservação ambiental."
                        }
                    ]
                }
            }
        ],
        8: [
            {
                "content": "Participar com sua unidade de um acampamento com estrutura de pioneiria, planejar o que deve ser levado e o que vai acontecer neste acampamento."
            },
            {
                "content": "Planejar, preparar e cozinhar três refeições ao ar livre."
            },
            {
                "content": "Construir e utilizar um móvel de acampamento em tamanho real, com nós e amarras."
            },
            {
                "content": "Completar uma especialidade, não realizada anteriormente, que possa ser contada para um dos Mestrados a seguir:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Aquática"
                        },
                        {
                            "content": "Esportes"
                        },
                        {
                            "content": "Atividades recreativas"
                        },
                        {
                            "content": "Vida campestre"
                        }
                    ]
                }
            }
        ],
        9: [
            {
                "content": "Completar uma especialidade, não realizada anteriormente, em uma das seguintes áreas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Atividades recreativas"
                        },
                        {
                            "content": "Ciência e saúde"
                        },
                        {
                            "content": "Habilidades domésticas"
                        },
                        {
                            "content": "Atividades profissionais"
                        }
                    ]
                }
            }
        ],
        10: [
            {
                "content": "Completar a especialidade de Mordomia."
            },
            {
                "content": "Ler o livro O Maior Discurso de Cristo e escrever uma página sobre o efeito da leitura em sua vida."
            },
            {
                "content": "Cumprir um dos seguintes itens:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Trazer dois amigos para assistir a duas diferentes reuniões da igreja."
                        },
                        {
                            "content": "Ajudar a planejar e participar de, no mínimo, quatro domingos em uma série de evangelismo jovem."
                        }
                    ]
                }
            },
            {
                "content": "Escrever uma página ou apresentar uma palestra de como influenciar amigos para Cristo."
            },
            {
                "content": "Observar durante o período de dois meses o trabalho dos diáconos, apresentando um relatório detalhado de suas atividades, contendo:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Cuidado da propriedade da igreja"
                        },
                        {
                            "content": "Cerimônia de lava-pés"
                        },
                        {
                            "content": "Cerimônia de batismo"
                        },
                        {
                            "content": "Recolhimento dos dízimos e ofertas"
                        }
                    ]
                }
            },
            {
                "content": "Completar o mestrado em Vida campestre."
            },
            {
                "content": "Projetar três tipos diferentes de abrigo, explicar seu uso e utilizar um deles em um acampamento."
            },
            {
                "content": "Assistir a um seminário ou apresentar uma palestra sobre dois dos seguintes temas:",
                "subRequirements": {
                    "type": 1,
                    "subRequirements": [
                        {
                            "content": "Aborto"
                        },
                        {
                            "content": "Bulliyng"
                        },
                        {
                            "content": "Violência"
                        },
                        {
                            "content": "Drogas"
                        },
                        {
                            "content": "Doenças sexualmente transmissíveis"
                        }
                    ]
                }
            },
            {
                "content": "Completar a especialidade de Liderança campestre."
            },
            {
                "content": "Completar a especialidade de Orçamento familiar."
            }
        ],
    }
}


def insert_requirements(cnx, cursor, requirements):
    try:
        class_id = requirements["classId"]
        requirement_groups = requirements["requirementGroups"]

        for requirement_group_id in requirement_groups:
            requirements = requirement_groups[requirement_group_id]

            for requirement in requirements:
                requirement_content = requirement["content"]

                sql = """
                    insert into requirement (requirementGroupId, classId, content)
                    value (%s, %s, %s);
                """

                values = (requirement_group_id, class_id, requirement_content)

                cursor.execute(sql, values)

                inserted_requirement_id = cursor.lastrowid

                sub_requirements = requirement.get("subRequirements")

                if sub_requirements is not None:
                    sub_requirement_type = sub_requirements["type"]

                    for sub_requirement in sub_requirements["subRequirements"]:
                        sub_requirement_content = sub_requirement["content"]

                        sql = """
                            insert into subrequirement (subrequirementTypeId, requirementId, content)
                            value (%s, %s, %s);
                        """

                        values = (sub_requirement_type, inserted_requirement_id, sub_requirement_content)

                        cursor.execute(sql, values)

        cnx.commit()

    except Exception as e:
        print(e)

        print(traceback.format_exc())
        
        print(sys.exc_info()[2])

        cnx.rollback()

    finally:
        cursor.close()

        cnx.close()


insert_requirements(cnx, cursor, guide_requirements)