"use client";

import Container from "@/components/Container";
import Message from "@/components/Message";
import BaseURL from "@/constants/BaseUrl";
import axios from "axios";
import Image from "next/image";
import { redirect } from "next/navigation";
import React, { useEffect, useState } from "react";
import toast from "react-hot-toast";

type listMessagesProps = {
  user: boolean;
  msg: string;
};

const ChatPage = () => {
  const [message, setMessage] = useState<string>("");
  const [messagesList, setMessagesList] = useState<listMessagesProps[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [email, setEmail] = useState<string>("");

  const handleDataChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setMessage(e.target.value);
  };

  const handleSendUserMessage = () => {
    if (message) {
      setMessagesList((prevList) => [
        ...prevList,
        { user: true, msg: message },
      ]);
      setMessage("");
      sendMessage();
    }
  };

  const handleAddBotMessage = (msg: string) => {
    if (msg) {
      setMessagesList((prevList) => [...prevList, { user: false, msg: msg }]);
    }
  };

  const sendMessage = async () => {
    try {
      setLoading(true);
      const res = await axios.post(
        `${BaseURL}/chat?prompt=${message}&userEmail=${email}`
      );
      handleAddBotMessage(res.data);
      setLoading(false);
    } catch (error: any) {
      if (error.status === 404) {
        setLoading(false);
        toast.error(error.response.data.detail);
        return;
      }
      setLoading(false);
      toast.error("Error while generating response");
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
    <Container className="my-5 mx-5 lg:mx-auto px-0 min-h-[94vh] border-dashed border-2 rounded-lg border-gray-500 relative flex">
      <div className="max-h-[80vh] overflow-y-auto w-full mb-24 p-4 flex flex-col gap-3">
        {messagesList.map((msg, idx) => (
          <div key={idx}>
            <Message message={msg.msg} user={msg.user} />
          </div>
        ))}

        {loading && <Message message="Thinking..." />}
      </div>

      <div className="absolute bottom-3 right-3 left-3">
        <div className="relative">
          <textarea
            autoFocus
            placeholder="Ask something..."
            className="bg-transparent border text-white w-full border-gray-700 rounded-lg p-4 relative resize-none"
            value={message}
            onChange={handleDataChange}
          />
          <Image
            src={"/send.png"}
            alt="send icon"
            width={40}
            height={40}
            className={`absolute bottom-7 right-3
              ${
                loading
                  ? "opacity-70 cursor-not-allowed"
                  : "hover:opacity-85 cursor-pointer"
              }
              `}
            onClick={loading ? () => {} : handleSendUserMessage}
          />
        </div>
      </div>
    </Container>
  );
};

export default ChatPage;
