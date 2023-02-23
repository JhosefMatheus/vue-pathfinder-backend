import { Injectable } from "@nestjs/common";
import { Pathfinder, Prisma } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
import { ICreatePathfinder, IDeletePathfinder, IGetPathfinder, IGetUserPathfinders } from "./interface";

@Injectable()
export class PathfinderService {
    constructor(private readonly prismaService: PrismaService) {}

    async createPathfinder(userId: number, name: string): Promise<ICreatePathfinder> {
        try {
            await this.prismaService.pathfinder.create({
                data: {
                    userId: userId,
                    name: name
                }
            });

            return {
                flag: true,
                message: "Desbravador criado com sucesso."
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2003") {
                    return {
                        flag: false,
                        message: "Id de usuário fornecido inválido."
                    }
                }
            }
        }
    }

    async getUserPathfinders(userId: string): Promise<IGetUserPathfinders> {
        try {
            const pathfinders: Pathfinder[] = await this.prismaService.pathfinder.findMany({
                where: {
                    userId: {
                        equals: parseInt(userId)
                    }
                }
            });

            return {
                flag: true,
                message: "Desbravadores encontrados com sucesso.",
                pathfinders
            }
        } catch (error) {
            return {
                flag: false,
                message: "Usuário com id inválido."
            }
        }
    }

    async deletePathfinder(pathfinderId: string): Promise<IDeletePathfinder> {
        try {
            await this.prismaService.pathfinder.delete({
                where: {
                    id: parseInt(pathfinderId)
                }
            });

            return {
                flag: true,
                message: "Desbravador excluído com sucesso."
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Id do desbravador inválido."
                    }
                }
            }
        }
    }

    async getPathfinder(userId: string, pathfinderId: string): Promise<IGetPathfinder> {
        try {
            const currentPathfinder = await this.prismaService.pathfinder.findFirstOrThrow({
                where: {
                    AND: {
                        userId: {
                            equals: parseInt(userId)
                        },
                        id: {
                            equals: parseInt(pathfinderId)
                        }
                    }
                }
            });

            return {
                flag: true,
                message: "Desbravador encontrado com sucesso.",
                currentPathfinder
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Id do usuário ou desbravador fornecido estão inválidos."
                    }
                }
            }
        }
    }

    async updatePathfinder(userId: string, pathfinderId: string, name: string) {
        try {
            await this.prismaService.pathfinder.update({
                where: {
                    id: parseInt(pathfinderId)
                },
                data: {
                    name: name
                }
            });
            
            return {
                flag: true,
                message: "Desbravador atualizado com sucesso"
            }
        } catch (error) {
            return {
                flag: false,
                message: "Id do desbravador fornecido inválido"
            }
        }
    }
}