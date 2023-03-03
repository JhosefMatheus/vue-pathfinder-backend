import { Injectable } from "@nestjs/common";
import { Requirement } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
import { IGetRequirements } from "./interface";

@Injectable()
export class RequirementService {
    constructor(private readonly prismaService: PrismaService) {}

    async getRequirements(classId: string, requirementGroupId: string): Promise<IGetRequirements> {
        const requirements: Requirement[] = await this.prismaService.requirement.findMany({
            where: {
                AND: {
                    classId: {
                        equals: parseInt(classId)
                    },
                    requirementGroupId: {
                        equals: parseInt(requirementGroupId)
                    }
                }
            }
        });

        return {
            flag: true,
            message: "Requisitos encontrados com sucesso.",
            requirements
        }
    }
}