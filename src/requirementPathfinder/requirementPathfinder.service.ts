import { Injectable } from "@nestjs/common";
import { PrismaService } from "src/prisma/prisma.service";
import { IGetRequirementPathfinder } from "./interface";
import { Prisma, Requirement, RequirementPathfinder } from "@prisma/client";

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

    async saveRequirements(pathfinderId: number, concludedRequirements: Requirement[], notConcludedRequirements: Requirement[]): Promise<void> {
        concludedRequirements.forEach(async requirement => {
            try {
                await this.prismaService.requirementPathfinder.findFirstOrThrow({
                    where: {
                        AND: {
                            requirementId: {
                                equals: requirement.id
                            },
                            pathfinderId: {
                                equals: pathfinderId
                            }
                        }
                    }
                });
            } catch (error) {
                console.log(error)
                if (error instanceof Prisma.PrismaClientKnownRequestError) {
                    if (error.code === "P2025") {
                        await this.prismaService.requirementPathfinder.create({
                            data: {
                                requirementId: requirement.id,
                                pathfinderId: pathfinderId
                            }
                        });
                    }
                }
            }
        });

        notConcludedRequirements.forEach(async requirement => {
            try {
                const currentRequirementPathfinder: RequirementPathfinder = await this.prismaService.requirementPathfinder.findFirstOrThrow({
                    where: {
                        AND: {
                            requirementId: {
                                equals: requirement.id
                            },
                            pathfinderId: {
                                equals: pathfinderId
                            }
                        }
                    }
                });

                await this.prismaService.requirementPathfinder.delete({
                    where: {
                        id: currentRequirementPathfinder.id
                    }
                });
            } catch (error) {
                if (error instanceof Prisma.PrismaClientKnownRequestError) {
                    if (error.code === "P2025") {

                    }
                }
            }
        });
    }
}