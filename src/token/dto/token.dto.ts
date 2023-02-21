import { IsNotEmpty, IsString } from "class-validator";

export class TokenDto {
    @IsString()
    @IsNotEmpty()
    authorization: string;

    [props: string]: any;
}