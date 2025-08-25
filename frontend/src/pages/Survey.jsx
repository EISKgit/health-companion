import { useState } from "react";
import { Button } from "@/components/ui/button";

export default function Survey() {
    const [step, setStep] = useState(1);

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-6">
            <div className="max-w-md w-full bg-white shadow-lg rounded-2xl p-6 text-center">
                <h1 className="text-xl font-bold mb-4">Daily Health Survey</h1>

                <p className="mb-6">Step {step} of 12</p>

                <Button
                    onClick={() => setStep(step + 1)}
                    disabled={step >= 12}
                >
                    Next
                </Button>
            </div>
        </div>
    );
}
