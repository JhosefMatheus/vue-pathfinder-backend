import { Controller, Get, Param, Res, UseGuards } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { Response } from "express";
import { IGetRequirementsParams } from "./interface";
import { RequirementService } from "./requirement.service";

@UseGuards(AuthGuard("jwt"))
@Controller("requirement")
export class RequirementController {
    constructor(private readonly requirementService: RequirementService) {}

    @Get("requirements/:classId/:requirementGroupId")
    async getRequirements(@Res() response: Response, @Param() params: IGetRequirementsParams) {
        const { classId, requirementGroupId } = params;

        console.log(classId, requirementGroupId);

        const { flag, message, requirements } = await this.requirementService.getRequirements(classId, requirementGroupId);

        if (flag) {
            return response.status(200).json({
                message,
                requirements
            });
        }

        return response.status(401).json({
            message
        });
    }
}