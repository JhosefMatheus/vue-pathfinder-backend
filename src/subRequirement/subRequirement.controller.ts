import { Controller, Get, Param, Res, UseGuards } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { Response } from "express";
import { IGetSubRequirementsParams } from "./interface";
import { SubRequirementService } from "./subRequirement.service";

@UseGuards(AuthGuard("jwt"))
@Controller("subRequirement")
export class SubRequirementController {
    constructor(private readonly subRequirementService: SubRequirementService) {}

    @Get("subRequirements/:requirementId")
    async getSubRequirements(@Res() response: Response, @Param() params: IGetSubRequirementsParams) {
        const { requirementId } = params;

        const { flag, message, subRequirements } = await this.subRequirementService.getSubRequirements(requirementId);

        if (flag) {
            return response.status(200).json({
                message,
                subRequirements
            });
        }

        return response.status(401).json({
            message
        });
    }
}