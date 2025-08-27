import { useState } from "react";
import { Button } from "@/components/ui/button";
import axios from "axios";


export default function Survey() {
    const [recommendationText, setRecommendationText] = useState("");

    const [step, setStep] = useState(1);
    const [answers, setAnswers] = useState({
        sleep_hours: 0,
        energy: 0,
        breakfast: null,
        water: 0,
        activity: 0,
        stress: 0,
        screen_time: null,
        mood: 0,
        substance_use: null,
        work_hours: 0,
        pain: null,
        pain_details: "",
        weather_effect: "",
    });








    const handleNext = () => {
        setStep(step + 1);
    };

    const handleSubmit = async () => {
        try {
            const payload = {
                ...answers,
                sleep_hours: parseInt(answers.sleep_hours, 10),
                water: parseInt(answers.water, 10),
                activity: parseInt(answers.activity, 10),
            };

            console.log("Submitting payload:", payload);

            const response = await axios.post(
                "http://127.0.0.1:8000/api/surveys/",
                answers
            );
            alert("Survey submitted! Recommendation: " + response.data.recommendation);
            // Save recommendation in state
            setRecommendationText(response.data.recommendation);
            console.log(response.data.recommendation);

        } catch (error) {
            console.error(error);
            alert("Failed to submit survey.");
        }
    };

    return (
        <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-6">
            <div className="max-w-md w-full bg-white shadow-lg rounded-2xl p-6 text-center">
                <h1 className="text-xl font-bold mb-4">Daily Health Survey</h1>
                <p className="mb-6">Step {step} of 12</p>

                {step === 1 && (
                    <div>
                        <p className="mb-4">How many hours did you sleep last night?</p>
                        <input
                            type="range"
                            min="0"
                            max="12"
                            value={answers.sleep_hours}
                            onChange={(e) =>
                                setAnswers({ ...answers, sleep_hours: e.target.value })
                            }
                            className="w-full"
                        />
                        <p className="mt-2 font-medium">{answers.sleep_hours} hours</p>
                    </div>
                )}
                {step === 2 && (
                    <div>
                        <p className="mb-4">How energetic do you feel today?</p>
                        <div className="flex justify-center space-x-4 text-3xl">
                            <span
                                className={`cursor-pointer ${answers.energy === 1 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, energy: 1 })}
                            >
                                😴
                            </span>
                            <span
                                className={`cursor-pointer ${answers.energy === 2 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, energy: 2 })}
                            >
                                😐
                            </span>
                            <span
                                className={`cursor-pointer ${answers.energy === 3 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, energy: 3 })}
                            >
                                😃
                            </span>
                        </div>
                        <p className="mt-3 font-medium">
                            {answers.energy === 1 && "Low energy"}
                            {answers.energy === 2 && "Okay"}
                            {answers.energy === 3 && "High energy"}
                        </p>
                    </div>
                )}

                {step === 3 && (
                    <div>
                        <p className="mb-4">Did you eat breakfast today?</p>
                        <div className="flex justify-center space-x-6">
                            <Button
                                variant={answers.breakfast === true ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, breakfast: true })}
                            >
                                Yes
                            </Button>
                            <Button
                                variant={answers.breakfast === false ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, breakfast: false })}
                            >
                                No
                            </Button>
                        </div>
                    </div>
                )}


                {step === 4 && (
                    <div>
                        <p className="mb-4">How many glasses of water did you drink yesterday?</p>
                        <input
                            type="range"
                            min="0"
                            max="12"
                            value={answers.water}
                            onChange={(e) => setAnswers({ ...answers, water: e.target.value })}
                            className="w-full"
                        />
                        <p className="mt-2 font-medium">{answers.water} glasses</p>
                    </div>
                )}



                {step === 5 && (
                    <div>
                        <p className="mb-4">
                            How many minutes of physical activity did you do yesterday?
                        </p>
                        <input
                            type="range"
                            min="0"
                            max="180"
                            step="10"
                            value={answers.activity}
                            onChange={(e) => setAnswers({ ...answers, activity: e.target.value })}
                            className="w-full"
                        />
                        <p className="mt-2 font-medium">{answers.activity} minutes</p>
                    </div>
                )}




                {step === 6 && (
                    <div>
                        <p className="mb-4">How stressed do you feel today?</p>
                        <div className="flex justify-center space-x-6 text-3xl">
                            <span
                                className={`cursor-pointer ${answers.stress === 1 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, stress: 1 })}
                            >
                                🙂
                            </span>
                            <span
                                className={`cursor-pointer ${answers.stress === 2 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, stress: 2 })}
                            >
                                😐
                            </span>
                            <span
                                className={`cursor-pointer ${answers.stress === 3 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, stress: 3 })}
                            >
                                😟
                            </span>
                        </div>
                        <p className="mt-3 font-medium">
                            {answers.stress === 1 && "Low stress"}
                            {answers.stress === 2 && "Moderate stress"}
                            {answers.stress === 3 && "High stress"}
                        </p>
                    </div>
                )}

                {step === 7 && (
                    <div>
                        <p className="mb-4">
                            Did you spend more than 2 hours on screens before bed yesterday?
                        </p>
                        <div className="flex justify-center space-x-6">
                            <Button
                                variant={answers.screen_time === true ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, screen_time: true })}
                            >
                                Yes
                            </Button>
                            <Button
                                variant={answers.screen_time === false ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, screen_time: false })}
                            >
                                No
                            </Button>
                        </div>
                    </div>
                )}


                {step === 8 && (
                    <div>
                        <p className="mb-4">How is your current mood?</p>
                        <div className="flex justify-center space-x-6 text-3xl">
                            <span
                                className={`cursor-pointer ${answers.mood === 1 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, mood: 1 })}
                            >
                                😞
                            </span>
                            <span
                                className={`cursor-pointer ${answers.mood === 2 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, mood: 2 })}
                            >
                                🙁
                            </span>
                            <span
                                className={`cursor-pointer ${answers.mood === 3 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, mood: 3 })}
                            >
                                😐
                            </span>
                            <span
                                className={`cursor-pointer ${answers.mood === 4 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, mood: 4 })}
                            >
                                🙂
                            </span>
                            <span
                                className={`cursor-pointer ${answers.mood === 5 ? "scale-125" : ""}`}
                                onClick={() => setAnswers({ ...answers, mood: 5 })}
                            >
                                😄
                            </span>
                        </div>
                        <p className="mt-3 font-medium">
                            {answers.mood === 1 && "Very sad"}
                            {answers.mood === 2 && "Sad"}
                            {answers.mood === 3 && "Neutral"}
                            {answers.mood === 4 && "Happy"}
                            {answers.mood === 5 && "Very happy"}
                        </p>
                    </div>
                )}



                {step === 9 && (
                    <div>
                        <p className="mb-4">Did you smoke or drink alcohol yesterday?</p>
                        <div className="flex justify-center space-x-6">
                            <Button
                                variant={answers.substance_use === true ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, substance_use: true })}
                            >
                                Yes
                            </Button>
                            <Button
                                variant={answers.substance_use === false ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, substance_use: false })}
                            >
                                No
                            </Button>
                        </div>
                    </div>
                )}


                {step === 10 && (
                    <div>
                        <p className="mb-4">How many hours did you work or study yesterday?</p>
                        <input
                            type="range"
                            min="0"
                            max="14"
                            value={answers.work_hours}
                            onChange={(e) =>
                                setAnswers({ ...answers, work_hours: parseInt(e.target.value) })
                            }
                            className="w-full"
                        />
                        <p className="mt-2 text-center font-semibold">
                            {answers.work_hours} hours
                        </p>
                    </div>
                )}

                {step === 11 && (
                    <div>
                        <p className="mb-4">Do you have any pain or discomfort today?</p>
                        <div className="flex justify-center space-x-6 mb-4">
                            <Button
                                variant={answers.pain === true ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, pain: true })}
                            >
                                Yes
                            </Button>
                            <Button
                                variant={answers.pain === false ? "default" : "outline"}
                                onClick={() => setAnswers({ ...answers, pain: false })}
                            >
                                No
                            </Button>
                        </div>

                        {answers.pain === true && (
                            <textarea
                                placeholder="Describe your pain/discomfort (optional)"
                                value={answers.pain_details}
                                onChange={(e) =>
                                    setAnswers({ ...answers, pain_details: e.target.value })
                                }
                                className="w-full p-2 border rounded-md"
                            />
                        )}
                    </div>
                )}

                {step === 12 && (
                    <div>
                        <p className="mb-4">How is the weather affecting you today?</p>
                        <div className="grid grid-cols-2 gap-4">
                            {["Fine", "Tired", "Bad", "Great"].map((option) => (
                                <Button
                                    key={option}
                                    variant={answers.weather_effect === option ? "default" : "outline"}
                                    onClick={() => setAnswers({ ...answers, weather_effect: option })}
                                >
                                    {option}
                                </Button>
                            ))}
                        </div>
                        <Button style={{ margin: '10px', marginTop: '20px' }} onClick={handleSubmit}>Submit Survey</Button>

                    </div>


                )}

                {recommendationText && (
                    <div className="mt-6 p-4 bg-green-100 text-green-800 rounded-md">
                        <h3 className="font-semibold mb-2">Your Lifestyle Tips:</h3>

                        <p>{recommendationText}</p>
                    </div>
                )}


                <div className="mt-6 flex justify-center">
                    <Button onClick={handleNext} disabled={step >= 12}>
                        Next
                    </Button>
                </div>
            </div>
        </div>
    );
}
