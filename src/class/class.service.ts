import { Class, Prisma } from "@prisma/client";
import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { IGetClasses } from "./dto";
import { IGetClassData } from "./interface/class.interface";

@Injectable()
export class ClassService {
    constructor(private readonly prismaService: PrismaService) {}

    async getClasses(): Promise<IGetClasses> {
        const classes: Class[] = await this.prismaService.class.findMany();

        return {
            classes
        }
    }

    async getClassData(id: string): Promise<IGetClassData> {
        try {
            const currentClass: Class = await this.prismaService.class.findFirstOrThrow({
                where: {
                    id: {
                        equals: parseInt(id)
                    }
                }
            });

            return {
                flag: true,
                message: "Classe encontrada com sucesso.",
                currentClass
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Id da classe fornecida inexistente."
                    }
                }
            }
        }
    }
}