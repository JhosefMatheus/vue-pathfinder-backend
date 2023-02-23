import { IsNotEmpty, IsNumber } from "class-validator";

export class CreatePathfinderDto {
    @IsNotEmpty()
    userId: number;

    @IsNotEmpty()
    name: string;
}

export class UpdatePathfinderDto {
    @IsNotEmpty()
    name: string;
}