export function expectDefined<T>(value: T | undefined): T {
  if (value === undefined) {
    throw new Error("Expected value to be defined.");
  }
  return value;
}
