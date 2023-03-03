import { Injectable } from "@nestjs/common";
import { Subrequirement } from "@prisma/client";
import { PrismaService } from "src/prisma/prisma.service";
import { IGetSubRequirements } from "./interface";

@Injectable()
export class SubRequirementService {
    constructor(private readonly prismaService: PrismaService) {}

    async getSubRequirements(requirementId: string): Promise<IGetSubRequirements> {
        const subRequirements: Subrequirement[] = await this.prismaService.subrequirement.findMany({
            where: {
                requirementId: {
                    equals: parseInt(requirementId)
                }
            }
        });

        return {
            flag: true,
            message: "Sub-requisitos encontrados com sucesso.",
            subRequirements
        }
    }
}