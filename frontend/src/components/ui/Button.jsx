import React from "react";

export function Button({ children, onClick, className }) {
    return (
        <button
            className={`bg-blue-500 text-white px-6 py-3 rounded-md hover:bg-blue-600 ${className}`}
            onClick={onClick}
        >
            {children}
        </button>
    );
}
