import { ReactNode } from "react";
import { twMerge } from "tailwind-merge";

type Props = {
  children: ReactNode;
  className?: string;
};

const Container = ({ className, children }: Props) => {
  return (
    <div className={twMerge("max-w-screen-lg mx-auto px-4", className)}>
      {children}
    </div>
  );
};

export default Container;
