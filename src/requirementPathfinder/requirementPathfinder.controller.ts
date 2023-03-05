import { Controller, Get, Res, Param } from "@nestjs/common";
import { Response } from "express";
import { IGetRequirementPathfinderParams } from "./interface";
import { RequirementPathfinderService } from "./requirementPathfinder.service";

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
}