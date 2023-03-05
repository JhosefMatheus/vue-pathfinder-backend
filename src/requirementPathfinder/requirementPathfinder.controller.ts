import { Controller, Get, Res, Param, UseGuards, Post, Body } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { Response } from "express";
import { RequirementPathfinderDto } from "./dto";
import { IGetRequirementPathfinderParams } from "./interface";
import { RequirementPathfinderService } from "./requirementPathfinder.service";

@UseGuards(AuthGuard("jwt"))
@Controller("requirementPathfinder")
export class RequirementPathfinderController {
    constructor(private readonly requirementPathfinderService: RequirementPathfinderService) {}

    @Get(":pathfinderId/:requirementId")
    async getRequirementPathfinder(@Res() response: Response, @Param() params: IGetRequirementPathfinderParams): Promise<Response> {
        const { pathfinderId, requirementId } = params;

        const { flag, message } = await this.requirementPathfinderService.getRequirementPathfinder(pathfinderId, requirementId);

        if (flag) {
            return response.status(200).json({
                message
            });
        }

        return response.status(401).json({
            message
        });
    }

    @Post("save")
    async saveRequirementsPathfinder(@Res() response: Response, @Body() saveRequirementPathfinderDto: RequirementPathfinderDto): Promise<Response> {
        const { pathfinderId, concludedRequirements, notConcludedRequirements } = saveRequirementPathfinderDto;

        await this.requirementPathfinderService.saveRequirements(pathfinderId, concludedRequirements, notConcludedRequirements);

        return response.status(200).json({
            message: "Requisitos do desbravador salvos com sucesso."
        });
    }
}