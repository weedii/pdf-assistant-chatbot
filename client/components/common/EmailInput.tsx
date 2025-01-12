"use client";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

const EmailInput = () => {
  const [email, setEmail] = useState<string>("");
  const [isAuth, setIsAuth] = useState<boolean>(false);
  const router = useRouter();

  const handleDataChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handleAuth = () => {
    if (typeof window !== undefined) {
      localStorage.setItem("email", email);
      router.push("/upload");
    }
  };

  const handleLogout = () => {
    if (typeof window !== undefined) {
      localStorage.removeItem("email");
      setIsAuth(false);
    }
  };

  useEffect(() => {
    if (typeof (window !== undefined)) {
      const email = localStorage.getItem("email");
      if (email) setIsAuth(true);
      else setIsAuth(false);
    }
  }, []);

  if (isAuth)
    return (
      <div className="flex flex-col gap-5">
        <p className="text-center font-semibold">
          Email: {localStorage.getItem("email")}
        </p>
        <button
          onClick={handleLogout}
          className="bg-blue-600 py-3 px-20 rounded-lg hover:bg-blue-700"
        >
          Logout
        </button>
      </div>
    );
  else
    return (
      <div className="flex flex-col justify-center gap-5 w-full">
        <label htmlFor="email" className="text-lg font-medium text-start">
          Enter you email
        </label>

        <input
          id="email"
          type="email"
          placeholder="Email"
          autoFocus
          className="bg-transparent py-3 px-5 border rounded-lg w-full"
          value={email}
          onChange={handleDataChange}
        />

        <button
          onClick={handleAuth}
          className="bg-blue-600 p-3 rounded-lg hover:bg-blue-700"
        >
          Authenticate
        </button>
      </div>
    );
};

export default EmailInput;
