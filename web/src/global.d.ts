declare module "*.css";
declare module "*.md" {
    const html: string;
    const metadata: object;
    const filename: string;
}

declare namespace Intl {
    class ListFormat {
        constructor(locale: string, args: { [key: string]: string });
        public format: (items: string[]) => string;
    }
}
