import { Requirement } from "@prisma/client";
import { IsNotEmpty } from "class-validator";

export class RequirementPathfinderDto {
    @IsNotEmpty()
    pathfinderId: number;

    @IsNotEmpty()
    concludedRequirements: Requirement[];

    @IsNotEmpty()
    notConcludedRequirements: Requirement[];
}