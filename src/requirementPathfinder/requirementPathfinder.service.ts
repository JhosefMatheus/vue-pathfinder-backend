import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { IGetRequirementPathfinder } from "./interface";
import { Prisma, RequirementPathfinder } from "@prisma/client";

@Injectable()
export class RequirementPathfinderService {
    constructor(private readonly prismaService: PrismaService) {}

    async getRequirementPathfinder(pathfinderId: string, requirementId: string): Promise<IGetRequirementPathfinder> {
        try {
            const requirementPathfinder: RequirementPathfinder = await this.prismaService.requirementPathfinder.findFirstOrThrow({
                where: {
                    AND: {
                        pathfinderId: {
                            equals: parseInt(pathfinderId)
                        },
                        requirementId: {
                            equals: parseInt(requirementId)
                        }
                    }
                }
            });

            return {
                flag: true,
                message: "Requisito do desbravador concluído."
            }
        } catch (error) {
            if (error instanceof Prisma.PrismaClientKnownRequestError) {
                if (error.code === "P2025") {
                    return {
                        flag: false,
                        message: "Requisito do desbravador não foi concluído."
                    }
                }
            }
        }
    }
}