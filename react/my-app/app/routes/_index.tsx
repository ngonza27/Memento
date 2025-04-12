import { AppLogo } from "~/components/app-logo";

export default function Index() {
  return (
    <section className="w-full bg-white min-h-screen flex flex-col">
      <nav className="flex items-center space-x-2 p-4">
        <AppLogo className="h-8 w-8 md:h-10 md:w-10" />
        <h1 className="text-xl  font-semibold text-zinc-900">Gitposter</h1>
      </nav>
    </section>
  );
}
