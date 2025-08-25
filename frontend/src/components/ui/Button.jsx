import * as React from "react";
import { cn } from "@/lib/utils";

export function Button({ className, variant = "default", ...props }) {
    return (
        <button
            className={cn(
                "px-4 py-2 rounded-md font-medium focus:outline-none focus:ring-2 focus:ring-offset-2",
                variant === "default" && "bg-blue-600 text-white hover:bg-blue-700",
                variant === "outline" && "border border-gray-300 text-gray-700 hover:bg-gray-100",
                className
            )}
            {...props}
        />
    );
}
