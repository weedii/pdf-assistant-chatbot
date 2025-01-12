"use client";

import axios from "axios";
import Image from "next/image";
import { redirect, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import toast from "react-hot-toast";
import Loader from "./common/Loader";
import BASEURL from "@/constants/BaseUrl";

const UploadFile = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [email, setEmail] = useState<string>("");
  const router = useRouter();

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];

    if (selectedFile) {
      if (selectedFile.type !== "application/pdf") {
        toast.error("Only PDF files are allowed.");
        setFile(null);
        return;
      } else {
        setFile(selectedFile);
      }
    }
  };

  const handleUploadFile = async () => {
    if (!file) {
      toast.error("No file found");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const res = await axios.post(
        `${BASEURL}/pdf?userEmail=${email}`,
        formData
      );
      console.log(res);
      setLoading(false);
      setFile(null);
      toast.success("File uploaded successfuly");
      router.push("/chat");
    } catch (error) {
      console.log(error);
      setLoading(false);
      toast.error("Error while saving PDF");
    }
  };

  useEffect(() => {
    if (typeof window !== undefined) {
      const email_ = localStorage.getItem("email");
      if (!email_) return redirect("/");
      else setEmail(email_);
    }
  }, []);

  return (
    <div className="flex flex-col items-center justify-center w-full gap-4">
      {loading ? (
        <div className="h-[80vh] w-full flex flex-col items-center justify-center gap-3">
          <Loader />
          <p className="font-semibold">Uploading PDF...</p>
        </div>
      ) : (
        <label
          htmlFor="dropzone-file"
          className={`flex flex-col items-center justify-center w-full border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-700
            ${file ? "h-[80vh]" : "h-[87vh] hover:bg-gray-800"}`}
        >
          {file ? (
            <div className="flex flex-col items-center justify-center py-5 gap-3">
              <Image
                src={"/pdficon.png"}
                alt="pdf icon"
                width={50}
                height={50}
              />
              <p className="font-semibold text-sm">{file.name}</p>
            </div>
          ) : (
            <div className="flex flex-col items-center justify-center pt-5 pb-6">
              <svg
                className="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 20 16"
              >
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
                />
              </svg>

              <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
                <span className="font-semibold">Click to upload</span> or drag
                and drop
              </p>
              <p className="text-xs text-gray-500 dark:text-gray-400">
                ONLY PDF FILES
              </p>
            </div>
          )}

          <input
            id="dropzone-file"
            type="file"
            className="hidden"
            onChange={handleFileChange}
            disabled={loading}
          />
        </label>
      )}

      {file && !loading && (
        <button
          onClick={handleUploadFile}
          disabled={loading}
          className="bg-blue-600 w-full py-3 rounded-lg font-semibold hover:bg-blue-700"
        >
          {loading ? "Loading..." : "Upload"}
        </button>
      )}
    </div>
  );
};

export default UploadFile;
