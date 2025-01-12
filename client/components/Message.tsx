import React from "react";

type Props = {
  message: string;
  user?: boolean;
};

const Message = ({ message, user }: Props) => {
  return (
    <div
      className={`min-w-[10rem] max-w-xl w-fit py-3 px-4 rounded-xl
        ${user ? "bg-blue-600 ml-auto" : "bg-slate-500"}`}
    >
      <p>{message}</p>
    </div>
  );
};

export default Message;
