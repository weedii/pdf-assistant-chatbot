import type { Metadata } from "next";
import "./globals.css";
import { Toaster } from "react-hot-toast";

export const metadata: Metadata = {
  title: "pdf-assistant-chatbot",
  description: "pdf-assistant-chatbot",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={``}>
        <main>{children}</main>
        <Toaster
          position="top-center"
          toastOptions={{
            style: {
              backgroundColor: "#282828",
              color: "white",
            },
          }}
        />
      </body>
    </html>
  );
}
