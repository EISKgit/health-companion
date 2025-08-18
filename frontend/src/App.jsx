import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "./components/ui/Button";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <motion.h1
        className="text-4xl font-bold mb-6"
        animate={{ rotate: 360 }}
        transition={{ duration: 2 }}
      >
        Hello Health Companion!
      </motion.h1>

      <Button onClick={() => setCount(count + 1)}>
        Click Me: {count}
      </Button>
    </div>
  );
}

export default App;
