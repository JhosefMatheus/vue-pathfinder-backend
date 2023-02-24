import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { RequirementGroup } from "@prisma/client"
import { IGetRequirementGroups } from "./interface";

@Injectable()
export class RequirementGroupService {
    constructor(private readonly prismaService: PrismaService) {}

    async getRequirementGroups(): Promise<IGetRequirementGroups> {
        const requirementGroups: RequirementGroup[] = await this.prismaService.requirementGroup.findMany();

        return {
            requirementGroups
        }
    }
}