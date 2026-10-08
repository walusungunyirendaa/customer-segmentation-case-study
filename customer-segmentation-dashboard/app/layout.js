import "./globals.css";

export const metadata = {
  title: "TelcoX Segment Dashboard",
  description:
    "Explore the five TelcoX customer segments. Fictional company, synthetic data.",
};

export const viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
