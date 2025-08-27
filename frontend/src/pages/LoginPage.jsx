const handleLogin = async () => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/api/token/", {
            username,
            password,
        });

        // Save JWT token in localStorage
        localStorage.setItem("token", response.data.access);

        alert("Login successful!");
        navigate("/survey"); // redirect to survey page
    } catch (error) {
        alert("Login failed!");
    }
};
